from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class TestUserModel(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(email='user@example.com', password='testpassword')
        self.assertEqual(user.email, 'user@example.com')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_employee)
        self.assertFalse(user.is_restaurant)

    def test_create_employee(self):
        employee = User.objects.create_employee(email='employee@example.com', password='testpassword')
        self.assertEqual(employee.email, 'employee@example.com')
        self.assertFalse(employee.is_staff)
        self.assertFalse(employee.is_superuser)
        self.assertTrue(employee.is_active)
        self.assertTrue(employee.is_employee)
        self.assertFalse(employee.is_restaurant)

    def test_create_restaurant(self):
        restaurant = User.objects.create_restaurant(email='restaurant@example.com', password='testpassword')
        self.assertEqual(restaurant.email, 'restaurant@example.com')
        self.assertFalse(restaurant.is_staff)
        self.assertFalse(restaurant.is_superuser)
        self.assertTrue(restaurant.is_active)
        self.assertFalse(restaurant.is_employee)
        self.assertTrue(restaurant.is_restaurant)

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(email='superuser@example.com', password='testpassword')
        self.assertEqual(superuser.email, 'superuser@example.com')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)
        self.assertFalse(superuser.is_employee)
        self.assertFalse(superuser.is_restaurant)
