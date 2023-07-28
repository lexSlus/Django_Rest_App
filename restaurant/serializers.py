from rest_framework import serializers

from restaurant.models import Restaurant, Menu, MenuVote


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'owner']
        read_only_fields = ['owner']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['items', 'restaurant']
        read_only_fields = ['restaurant']


class MenuVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuVote
        fields = ['menu', 'user']
