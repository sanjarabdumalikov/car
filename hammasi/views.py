from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import car,car_shop
from rest_framework.response import Response
from .serializer import carserializer,car_shopserilizer
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated



class AllCreate(generics.ListCreateAPIView):
    queryset = car.objects.all()
    serializer_class = carserializer
    permission_classes = IsAuthenticated


class DetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = car.objects.all()
    serializer_class = carserializer
    permission_classes = IsAuthenticated
