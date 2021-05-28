'''
Source:

Author: Raja CSP
'''

import random
import json
from pprint import pprint
import random

# Local import


FILEPATH = 'player.json'

def get_random_digit(digit = 6):

    min = (pow(10, (digit - 1)))
    max = (pow(10, (digit))) - 1

    # print(f'get_random_digit : min [{min}], max [{max}]')

    return random.randint(min, max)

def get_json_data():

    with open(FILEPATH) as json_file:
        data = json.load(json_file)
        
        # print(data)

    return data

def store_json_data(data):

    with open(FILEPATH, 'w') as outfile:
        json.dump(data, outfile)

def get_game_players(game_code):

    player_dict = get_json_data()

    # pprint(player_dict)

    if(game_code in player_dict):
        return player_dict[game_code]

    return None

def create_game_with_players(
    player_1_name, 
    player_2_name
):

    game_postcode   = get_random_digit()

    game_code       = "gc_" + str(game_postcode)

    game_players = {
        "player_1" : {
                "name" : player_1_name,
                "gender" : "Unknown"
            },
            "player_2" : {
                "name" : player_2_name,
                "gender" : "Unknown"
            }
        }


    old_game_json = get_json_data()

    old_game_json[game_code] = game_players

    # store into json
    store_json_data(old_game_json)

    # print(ch_meter)
    # return c_city

    return game_code

def startpy():

    local_player = get_game_players("gc_182248")
    print(local_player)

    # get_random_digit(5)

    # create_game_with_players("Vedha", "Ishita")


if __name__ == "__main__":
    startpy()
    