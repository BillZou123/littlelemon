from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'bookings', views.BookingViewSet) # we need this since BookingViewSet  is not a regular Django view; it's a Django REST framework ViewSet, specifically a ModelViewSet.

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('hello', views.hello_world),
     path('index', views.index),
     path('menu', views.MenuItemsView.as_view()),
     path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
     path((''), include(router.urls)),
     

]