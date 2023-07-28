from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import UserSerializer, EmployeeSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateEmployeeView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('vote')
        else:
            error_message = "Invalid email or password. Please try again."
            return render(request, 'login_page.html', {'error_message': error_message})
    else:
        return render(request, 'login_page.html')


def logout_page(request):
    logout(request)
    return redirect('login')
