from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import response
from rest_framework import status

from CarDealershipAPI import models
from CarDealershipAPI import serializers


class carProfileViewset (viewsets.ModelViewSet):
    serializer_class = serializers.carProfileSerializer
    queryset = models.carProfile.objects.all()