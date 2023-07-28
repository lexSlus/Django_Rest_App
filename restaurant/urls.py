from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('restaurant', views.RestaurantView)
router1 = DefaultRouter()
router1.register('menu', views.MenuView)
urlpatterns = [
    path('', include(router.urls)),
    path('', include(router1.urls)),
]
