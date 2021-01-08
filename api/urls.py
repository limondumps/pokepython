from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import Pokemon_SearchView

urlpatterns = [
    path('pokemon_search/<str:pokemon_name>/', Pokemon_SearchView.as_view()),
]