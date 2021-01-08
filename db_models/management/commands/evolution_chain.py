from django.core.management.base import BaseCommand, CommandError
from db_models.models import Pokemon_Stat, Pokemon, Evolution_Chain
import requests
import json

def pokemon_detail(pokemon):
    pokemon_dict = None
    url_pokemon_detail = 'https://pokeapi.co/api/v2/pokemon/'+ pokemon+'/'
    response = requests.get(url = url_pokemon_detail)
    if (response.status_code==200):
        pokemon_dict = {}
        json_response = response.json()
        pokemon_dict["id"] = json_response["id"]
        pokemon_dict["height"] = json_response["height"]
        pokemon_dict["weight"] = json_response["weight"]
        pokemon_dict["stats"] = []
        for stat in json_response["stats"]:
            pokemon_dict["stats"].append({"base_stat": stat["base_stat"], "effort": stat["effort"], "name": stat["stat"]["name"], "url": stat["stat"]["url"]})
    return pokemon_dict

class Command(BaseCommand):
    help = 'Receives only one parameter ID, representing the Evolution Chain'
    
    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='ID of the Evolution Chain')
    
    def handle(self, *args, **kwargs):
        evolution_chain_id = int(kwargs['id'])
        url_evolution_chain = 'https://pokeapi.co/api/v2/evolution-chain/'+ str(evolution_chain_id)+'/'
        response = requests.get(url = url_evolution_chain)
        
        if (response.status_code==200):
            json_response = response.json()
            
            evolution_chain_pokemons = []
            
            ##Firts Pokemon in the evolution chain
            evolution_chain_pokemons.append( {**pokemon_detail(json_response["chain"]["species"]["name"]),**{"name": json_response["chain"]["species"]["name"], "url": json_response["chain"]["species"]["url"]}})
            
            ##aux pointer
            evolves_to_pointer = json_response["chain"]
            
            ##More Pokemons in the evolution chain
            while len(evolves_to_pointer["evolves_to"])>0:
                evolution_chain_pokemons.append( {**pokemon_detail(evolves_to_pointer["evolves_to"][0]["species"]["name"]),**{"name": evolves_to_pointer["evolves_to"][0]["species"]["name"], "url": evolves_to_pointer["evolves_to"][0]["species"]["url"]}})
                evolves_to_pointer = evolves_to_pointer["evolves_to"][0]
            
            (obj_evolution_chain, message) = Evolution_Chain.save_evolution_chain(url_evolution_chain,evolution_chain_id,evolution_chain_pokemons)
                      
            self.stdout.write(message+"\n")
            self.stdout.write("Evolution Chain ID: " + str(obj_evolution_chain.id)+ "\n")
            self.stdout.write("Evolution Chain Url: " + str(obj_evolution_chain.url)+ "\n")
            self.stdout.write("Evolution Chain Pokemons: \n")
            for pokemon in obj_evolution_chain.evolution_chain_pokemons.all():
                self.stdout.write(" "*5 + ("Pokemon Name: " + pokemon.name)+ "\n")
                self.stdout.write(" "*5 + ("Pokemon ID: " + str(pokemon.id))+ "\n")
                self.stdout.write(" "*5 + ("Pokemon Height: " + str(pokemon.height))+ "\n")
                self.stdout.write(" "*5 + ("Pokemon Wieght: " + str(pokemon.weight))+ "\n")
                self.stdout.write(" "*5 + ("Pokemon Url: " + pokemon.url)+ "\n")
                self.stdout.write(" "*5 + ("Pokemon Base Stats: \n"))
                
                for stat in pokemon.pokemon_stats.all():
                    self.stdout.write(" "*10 + "Stats Name:" + stat.name+ "\n")
                    self.stdout.write(" "*10 + "Stats :" + str(stat.base_stat) + "\n")
                    self.stdout.write(" "*10 + "Stats Effort:"+ str(stat.effort)+ "\n")
                    self.stdout.write(" "*10 + "Stats Url:" + stat.url+ "\n")
                    self.stdout.write("\n")
                
                self.stdout.write("\n")
                    
        else:
            raise CommandError('Evolution Chain ID "%s" does not exist' % str(evolution_chain_id))