from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import  RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import *
from .serializers import *
from rest_framework import viewsets, permissions


# Create your views here.
@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})



def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 