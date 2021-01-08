# POKEPYTHON

This is a Back-end Technical Test.

The main functionalities are:

* Use of the requests module to obtain information from an api.
* Create a custom command to save your query information.
* Publish an API VIEW to query the pokemon information.

### Installing

```
pip install Django
pip install requests
pip install djangorestframework
```

* Password of superuser
```
http://192.168.0.18:8888/admin
```

```
* user: pokedemo 
* password: pokedemo
```

## Running

* Start the server
```
python manage.py runserver 192.168.0.18:8888
```

* Adding a Evolution Chain ID 1
```
python manage.py evolution_chain 1
```
```
(envmo) [root@raptor pokepython]# python manage.py evolution_chain 13
Evolution Chain ID: 13 saved in the database.
Evolution Chain ID: 13
Evolution Chain Url: https://pokeapi.co/api/v2/evolution-chain/13/
Evolution Chain Pokemons:
     Pokemon Name: nidoran-m
     Pokemon ID: 32
     Pokemon Height: 5.00
     Pokemon Wieght: 90.00
     Pokemon Url: https://pokeapi.co/api/v2/pokemon-species/32/
     Pokemon Base Stats:
          Stats Name:hp
          Stats :46
          Stats Effort:0
          Stats Url:https://pokeapi.co/api/v2/stat/1/

          Stats Name:attack
          Stats :57
          Stats Effort:1
          Stats Url:https://pokeapi.co/api/v2/stat/2/

          Stats Name:defense
          Stats :40
          Stats Effort:0
          Stats Url:https://pokeapi.co/api/v2/stat/3/

          Stats Name:special-attack
          Stats :40
          Stats Effort:0
          Stats Url:https://pokeapi.co/api/v2/stat/4/

          Stats Name:special-defense
          Stats :40
          Stats Effort:0
          Stats Url:https://pokeapi.co/api/v2/stat/5/

          Stats Name:speed
          Stats :50
          Stats Effort:0
          Stats Url:https://pokeapi.co/api/v2/stat/6/


     Pokemon Name: nidorino
     Pokemon ID: 33
     Pokemon Height: 9.00
     Pokemon Wieght: 195.00
     Pokemon Url: https://pokeapi.co/api/v2/pokemon-species/33/
     Pokemon Base Stats:
          Stats Name:hp
```

* Request information about "pokemon name"
```
http://192.168.0.18:8888/api/pokemon_search/butterfree/
```

{"id": 12, "name": "butterfree", "height": "11.00", "weight": "320.00", "url": "https://pokeapi.co/api/v2/pokemon-species/12/", "stats": [{"name": "hp", "base_stat": 60, "effort": 0, "url": "https://pokeapi.co/api/v2/stat/1/"}, {"name": "attack", "base_stat": 45, "effort": 0, "url": "https://pokeapi.co/api/v2/stat/2/"}, {"name": "defense", "base_stat": 50, "effort": 0, "url": "https://pokeapi.co/api/v2/stat/3/"}, {"name": "special-attack", "base_stat": 90, "effort": 2, "url": "https://pokeapi.co/api/v2/stat/4/"}, {"name": "special-defense", "base_stat": 80, "effort": 1, "url": "https://pokeapi.co/api/v2/stat/5/"}, {"name": "speed", "base_stat": 70, "effort": 0, "url": "https://pokeapi.co/api/v2/stat/6/"}], "evolutions": [{"id": 10, "name": "caterpie", "evolution_type": "Preevolution"}, {"id": 11, "name": "metapod", "evolution_type": "Preevolution"}]}