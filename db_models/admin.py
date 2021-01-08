from django.contrib import admin
from .models import Pokemon_Stat, Pokemon, Evolution_Chain


@admin.register(Pokemon_Stat)
class Pokemon_StatAdmin(admin.ModelAdmin):
    list_display = ['pokemon','stat']
    
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['name','url']

@admin.register(Evolution_Chain)
class Evolution_ChainAdmin(admin.ModelAdmin):
    list_display = ['id','url']