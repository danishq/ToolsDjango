from django.shortcuts import render
from geopy.geocoders import Nominatim
import requests  # ✅ Ensure this is present

def Weather(request):
    return render(request, "Weather/weather.html")
