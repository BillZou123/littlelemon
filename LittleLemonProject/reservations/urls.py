from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
    path('hello', views.hello_world),
     path('index', views.index),
     path('menu', views.MenuItemsView.as_view()),
     path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
     path((''), include(router.urls)),
     

]