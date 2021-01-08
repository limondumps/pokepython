from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from django.db import connection
from rest_framework import generics
from datetime import datetime
from db_models.models import Pokemon_Stat, Pokemon, Evolution_Chain
from django.http import HttpResponse, JsonResponse

import pytz
import time

class Pokemon_SearchView(APIView):

    def get(self, request, pokemon_name):
        
        if Pokemon.objects.filter(name = pokemon_name).count() == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        else:
            pokemon_info = {}
            pokemon = Pokemon.objects.filter(name = pokemon_name).first()
            
            pokemon_info["id"] = pokemon.id
            pokemon_info["name"] = pokemon.name
            pokemon_info["height"] = pokemon.height
            pokemon_info["weight"] = pokemon.weight
            pokemon_info["url"] = pokemon.url
            
            pokemon_info["stats"] = []
            for stat in pokemon.pokemon_stats.all():
                pokemon_info["stats"].append({"name": stat.name, "base_stat": stat.base_stat, "effort": stat.effort, "url": stat.url})
            
            pokemon_info["evolutions"] = []
            ##Preevolution / Evolution
            bool_evolution = False
            for iter_pokemon in pokemon.evolution_chain.evolution_chain_pokemons.all().order_by('id'):
                if pokemon.name==iter_pokemon.name:
                    bool_evolution = True
                    continue
                    
                pokemon_info["evolutions"].append({"id": iter_pokemon.id, "name": iter_pokemon.name, "evolution_type" : 'Evolution' if bool_evolution else 'Preevolution'})

            
            return JsonResponse(pokemon_info, safe=False)
        