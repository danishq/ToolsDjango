from django.contrib import admin
from django.urls import path,include
from . import views
# form .views import get_weather

urlpatterns = [
    path('',views.Weather, name='weather')
    # path('', get_weather, name='get_weather'),
]
