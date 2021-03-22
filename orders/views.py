from django.shortcuts import render
from rest_framework import generics
from .serializer import OrderSerializer
from .models import Orders
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class OrderList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer