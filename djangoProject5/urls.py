"""
URL configuration for djangoProject5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import CreateUserView, CreateEmployeeView, login_page, logout_page
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from restaurant.views import CurrentDayMenuView, VoteMenus, quantity_of_votes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_rest/', CreateUserView.as_view(), name='create_rest'),
    path('create_employee/', CreateEmployeeView.as_view(), name='create_employee'),
    path('api/', include('restaurant.urls')),

    path('today_menu/', CurrentDayMenuView.as_view({'get': 'list'}), name='today_menu'),
    path('vote/', VoteMenus, name='vote'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('quantity_of_votes/', quantity_of_votes, name='quantity'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
