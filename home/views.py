from django.shortcuts import redirect
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Attractions, DosDonts, NearbyHotels, ThingsToExplore
from .serializer import AttractionsSerializer, DosDontsSerializer, NearbyHotelsSerializer, ThingsToExploreSerializer


class AttractionsViewSet(viewsets.ModelViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer


class DosDontsViewSet(viewsets.ModelViewSet):
    queryset = DosDonts.objects.all()
    serializer_class = DosDontsSerializer


class NearbyHotelsViewSet(viewsets.ModelViewSet):
    queryset = NearbyHotels.objects.all()
    serializer_class = NearbyHotelsSerializer


class ThingsToExploreViewSet(viewsets.ModelViewSet):

    queryset = ThingsToExplore.objects.all()
    serializer_class = ThingsToExploreSerializer


