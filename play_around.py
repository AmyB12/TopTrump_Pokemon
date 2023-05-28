import json
import requests
import random

# # testing and understanding the API and request methods
# pokemon_req = requests.get('https://pokeapi.co/api/v2/pokemon')
# pokemon = pokemon_req.json()
# print(pokemon)
#
# # play around with other set
# base_url = "https://cat-fact.herokuapp.com"
# facts = "/facts/random?animal_type=cat&amount=500"
# response = requests.get(base_url + facts)
# response_list = response.json()
# data = []
# for response in response_list:
#     data.append({
#         "used": response.get('used'),
#         "source": response.get('source'),
#         "text": response.get('text'),
#         "updatedAt": response.get('updatedAt'),
#         "createdAt": response.get('createdAt'),
#         "user": response.get('user')
#
#     })
# print(data)