from django.db import models
from django.db import transaction

class Pokemon_Stat(models.Model):
    pokemon = models.ForeignKey('Pokemon', related_name = 'pokemon_stats', on_delete = models.CASCADE, blank = True, null = True)
    stat = models.CharField(max_length = 100, blank = True, null = True)
    url = models.CharField(max_length = 100, blank = True, null = True)
    base_stat = models.IntegerField(blank = True, null = True)
    effort = models.IntegerField(blank = True, null = True)
    name = models.CharField(max_length = 100, blank = True, null = True)

class Pokemon(models.Model):
    name = models.CharField(max_length = 100, primary_key = True)
    id = models.IntegerField(blank = True, null = True)
    height = models.DecimalField(max_digits = 10, decimal_places = 2, blank = True, null = True)
    weight = models.DecimalField(max_digits = 10, decimal_places = 2, blank = True, null = True)
    url = models.CharField(max_length = 100, blank = True, null = True)
    evolution_chain = models.ForeignKey('Evolution_Chain', related_name = 'evolution_chain_pokemons', on_delete = models.CASCADE, blank = True, null = True)
    
class Evolution_Chain(models.Model):
    id = models.IntegerField(primary_key = True)
    url = models.CharField(max_length = 100, blank = True, null = True)
    
    @staticmethod
    @transaction.atomic
    def save_evolution_chain(url_evolution_chain,evolution_chain_id, evolution_chain_pokemons):
       obj_evolution_chain = None
       message = ""
       if Evolution_Chain.objects.filter(id = evolution_chain_id).count() == 0:
           
           obj_evolution_chain = Evolution_Chain()
           obj_evolution_chain.id = evolution_chain_id
           obj_evolution_chain.url = url_evolution_chain
           obj_evolution_chain.save()
           
           for pokemon in evolution_chain_pokemons:
               obj_pokemon = Pokemon()
               obj_pokemon.name = pokemon["name"]
               obj_pokemon.id = pokemon["id"]
               obj_pokemon.height = pokemon["height"]
               obj_pokemon.weight = pokemon["weight"]
               obj_pokemon.url = pokemon["url"]
               obj_pokemon.evolution_chain = obj_evolution_chain
               obj_pokemon.save()
               
               for stat in pokemon["stats"]:
                   obj_stat = Pokemon_Stat()
                   obj_stat.base_stat = stat["base_stat"]
                   obj_stat.effort = stat["effort"]
                   obj_stat.name = stat["name"]
                   obj_stat.url = stat["url"]
                   obj_stat.pokemon = obj_pokemon
                   obj_stat.save()

           message = "Evolution Chain ID: " + str(evolution_chain_id)+" saved in the database."
       else:
           message = "Evolution Chain ID: " + str(evolution_chain_id)+" does exits in the database."
           obj_evolution_chain  = Evolution_Chain.objects.filter(id = evolution_chain_id).first()
       return (obj_evolution_chain,message)