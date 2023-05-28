import json
import requests
import random


# having the functions act outside the class was easier coding wise and easier to control when testing parts of it
# Pulls random number to, pick the Pokemon from the API at random
def create_id():
    poke_id = random.randint(1, 151)  # Number from 1 to 151 (they didn't add the newer pokemons)
    return poke_id


# This would find the pokemon based on the random id created.
def get_pokemon():
    pokemon_api = 'https://pokeapi.co/api/v2/pokemon/' + str(create_id())
    poke_request = requests.get(pokemon_api)  # The get() method sends a GET request to the specified url.
    pokemon = poke_request.json()  # get the json files as dictionaries
    return pokemon


# This class is to collect the retrieved information from the api and find the ones I want to use in the game.
# creating individual objects for each Pokemon
class Pokemon:
    def __init__(self):
        pokemon = get_pokemon()
        self.name = pokemon['name'].title()
        self.id = pokemon['id']
        self.order = pokemon['order']
        self.height = pokemon['height']
        self.weight = pokemon['weight']
        self.base_experience = pokemon['base_experience']


# Compare the stats chosen by user and, depending on the value determine if the player get points during the match
def compare_points(player, competitor):
    if player > competitor:
        won = 1
        print('You Won!')
    elif player == competitor:
        won = 0
        print("It's a Draw")
    else:
        won = 0
        print('You Lost!')
    return won


# this is the compare the states depending on the option, compare_points will tell if the player or the competitor won
# results are then later collated.
def compare_stats(stat, player_pokemon, competitor_pokemon):
    if stat == 'id':
        result = compare_points(player_pokemon.id, competitor_pokemon.id)
        return result
    elif stat == 'order':
        result = compare_points(player_pokemon.order, competitor_pokemon.order)
        return result
    elif stat == 'height':
        result = compare_points(player_pokemon.height, competitor_pokemon.height)
        return result
    elif stat == 'weight':
        result = compare_points(player_pokemon.weight, competitor_pokemon.weight)
        return result
    elif stat == 'base_experience':
        result = compare_points(player_pokemon.base_experience, competitor_pokemon.base_experience)
        return result


# finally now to score and tell who wins, the competitor and player pokemon is determined, print the stats for the
# player and show the options they would use during battle
def play_game(scoring):
    competitor_pokemon = Pokemon()
    player_pokemon = Pokemon()
    print(
        f'Your Pokemon: \n Pokemon: {player_pokemon.name} (ID: {player_pokemon.id}) '
        f'\n Order: {player_pokemon.order} '
        f'\n Height: {player_pokemon.height}'
        f'\n Weight: {player_pokemon.weight}'
        f'\n Base Experience: {player_pokemon.base_experience} ')
    print(f'Your opponent chose: {competitor_pokemon.name}')

    choose_stat = str(
        input('Which stat would you like to use? ID / Order / Height / Weight / Base_Experience \n')).lower()

    # result calls the compare_stats function and input the choice and pokemon, this will run it through the
    # compare_points giving the points
    result = compare_stats(choose_stat, player_pokemon, competitor_pokemon)
    scoring += int(result)  # add to the score for each game played
    print(f'Current Score: {scoring}')  # show player the points after each match
    play_game(scoring)  # call this function again to keep going


# let the games begin
score = 0
play_game(score)
