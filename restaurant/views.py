from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import date
from .models import Restaurant, Menu, MenuVote
from .serializers import RestaurantSerializer, MenuSerializer, MenuVoteSerializer


class RestaurantView(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MenuView(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        restaurant = Restaurant.objects.get(owner=user)
        serializer.save(restaurant=restaurant)


class CurrentDayMenuView(viewsets.ReadOnlyModelViewSet):
    serializer_class = MenuSerializer

    def get_queryset(self):
        today = date.today()
        name = self.request.user
        return Menu.objects.filter(date=today, restaurant__owner=name)


@login_required
def VoteMenus(request):
    today = date.today()
    current_menus = Menu.objects.filter(date=today)
    if request.method == 'POST':
        menu_id = request.POST.get('menu_id')
        if menu_id:
            menu = Menu.objects.get(pk=menu_id)
            user = request.user
            if not MenuVote.objects.filter(user=user, menu=menu).exists():
                vote = MenuVote(user=user, menu=menu)
                vote.save()
                return HttpResponse('thank_you')
            return HttpResponse('already_voted')
        else:
            return HttpResponse('no data')
    return render(request, 'page_to_vote.html', {'menus': current_menus})


from django.db.models import Count


@api_view(['GET'])
def quantity_of_votes(request):
    today = date.today()
    current_menus = Menu.objects.filter(date=today)
    menu_votes = MenuVote.objects.filter(menu__in=current_menus)
    menu_votes_count = menu_votes.values('menu').annotate(count=Count('id'))
    menu_votes_dict = {entry['menu']: entry['count'] for entry in menu_votes_count}
    max_value = max(menu_votes_dict, key=lambda k: menu_votes_dict[k])
    menu_votes_dict['winner'] = max_value
    return Response(menu_votes_dict)
