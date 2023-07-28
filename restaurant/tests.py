from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import Restaurant, Menu, MenuVote
from restaurant.serializers import RestaurantSerializer, MenuSerializer, MenuVoteSerializer

User = get_user_model()


class TestRestaurantModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpassword')

    def test_restaurant_be_created(self):
        restaurant = Restaurant.objects.create(name='TestName', owner_id=self.user.id)
        self.assertEqual(restaurant.name, 'TestName')
        self.assertEqual(restaurant.owner, self.user)


class TestMenuModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpassword')
        self.restaurant = Restaurant.objects.create(name='TestRestaurant', owner=self.user)

    def test_menu_creation(self):
        menu = Menu.objects.create(restaurant=self.restaurant, items='abc')
        self.assertEqual(menu.items, 'abc')
        self.assertEqual(menu.restaurant, self.restaurant)


class TestMenuVoteModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpassword')
        self.restaurant = Restaurant.objects.create(name='TestRestaurant', owner=self.user)
        self.menu = Menu.objects.create(restaurant=self.restaurant, items='abc')

    def test_menuvote_creation(self):
        menuvote = MenuVote.objects.create(user=self.user, menu=self.menu)
        self.assertEqual(menuvote.user, self.user)
        self.assertEqual(menuvote.menu, self.menu)

    def test_new_vote(self):
        newmenu = Menu.objects.create(restaurant=self.restaurant, items='abcd')
        menuvote = MenuVote.objects.create(user=self.user, menu=self.menu)
        self.assertNotEqual(newmenu.items, menuvote.menu.items)


class SerializerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpassword')
        self.restaurant = Restaurant.objects.create(name='Test Restaurant', owner=self.user)
        self.menu = Menu.objects.create(items='Burger, Pizza', restaurant=self.restaurant)

    def test_restaurant_serializer(self):
        serializer = RestaurantSerializer(self.restaurant)
        expected_data = {'name': 'Test Restaurant', 'owner': self.user.id}
        self.assertEqual(serializer.data, expected_data)

    def test_menu_serializer(self):
        serializer = MenuSerializer(self.menu)
        expected_data = {'items': 'Burger, Pizza', 'restaurant': self.restaurant.id}
        self.assertEqual(serializer.data, expected_data)

    def test_menu_vote_serializer(self):
        menu_vote = MenuVote.objects.create(menu=self.menu, user=self.user)
        serializer = MenuVoteSerializer(menu_vote)
        expected_data = {'menu': self.menu.id, 'user': self.user.id}
        self.assertEqual(serializer.data, expected_data)
