import json

WORDS_JSON_PATH = 'words.json'

def store_word(word, score, game_code, player_index):

    new_word_dict = {
        'word' : word,
        'score' : score
    }

    data = get_json_data()

    player_name = 'player_'+str(player_index)

    # if list is not available, create a dummy list
    if(game_code not in data):
        data[game_code] = {
            'player_'+str(1) : [],
            'player_'+str(2) : []
        }

    data[game_code][player_name].append(new_word_dict)

    with open(WORDS_JSON_PATH, 'w') as outfile:
        json.dump(data, outfile)

def get_json_data():

    with open(WORDS_JSON_PATH) as json_file:
        data = (json.load(json_file))

    return data    

if __name__ == "__main__":    
   get_json_data()