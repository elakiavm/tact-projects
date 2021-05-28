'''
Source:

Author: Serkinti Team
    Sharon
    Bairavi
    Talha
    Vedha
    Ishita
    Prakash
    Ana Jessica
    Praabindh
    Elakia
    Raja (Mentor)
'''

from flask import Flask, render_template, request, jsonify
import random
import json
import json_store
from redis import Redis

# Local Import
import serkinti_text_engine as ste
import related_words as rw
import store_redis as sr
import business

app  = Flask(__name__)
PORT = 3023

redis = Redis(host = 'redis', port = 6379)

'''
    http://0.0.0.0:3023/game/<game_code>
'''
@app.route("/game/<game_code>", methods=["GET","POST"]) #microservice added but pls check functionality in frontend
def page_game_by_gamecode(game_code):

    #print('game_code : ', game_code)
    data_players = json_store.get_game_players(game_code)

    # result = {
    #     "players" : players
    # }

    player_2_name = data_players["player_2"]["name"]
    
    if(player_2_name == "bot"):
        return render_template ("bot.html")

    return render_template(
        "game.html",
        game_code = game_code
        # , result = result
    )

'''
    http://0.0.0.0:3023/api/game/<game_code>
'''
@app.route("/api/game/<game_code>", methods=["GET","POST"]) #Microservice added for this function
def api_game_by_gamecode(game_code):

    players = json_store.get_game_players(game_code)

    players_list = []

    players_list.append(
        players['player_1']['name']
    )
    players_list.append(
        players['player_2']['name']
    )
    
    result = {
        "game_code"     : game_code,
        "players"       : players,
        "players_list"  : players_list,
        "Greetings"     : "Serkinti welcomes you"
    }

    return jsonify(result)

    
'''
    http://0.0.0.0:3023/api/get/word/score
    http://0.0.0.0:3023/api/get/word/score?word=one&player_index=1&game_code=gc_23
'''
@app.route("/api/get/word/score", methods=["GET","POST"]) #Microservice added for this function
def api_get_word_score():

    word            = request.values.get('word')
    game_code       = request.values.get('game_code')
    player_index    = request.values.get('player_index')

    # score   = ste.get_word_score(word, game_code, player_index)

    score_obj = business.get_word_score_ms_api(word)
    

    result = {
        "word"     : word,
        "score"    : score_obj["score"]
    }

    #print('result : ', result)

    return jsonify(result)

'''
    http://0.0.0.0:3023/
'''
@app.route("/lobby", methods=["GET", "POST"])
def page_players():

    if request.method == 'GET':
        
        return render_template("index.html") 

    # by default post
    player_1_name = request.values.get("player_1_name")
    player_2_name = request.values.get("player_2_name")

    # store into json
    game_code = json_store.create_game_with_players(player_1_name, player_2_name)

    result = {
        "game_code" : game_code,
        "status" : "updated"
    }

    # return jsonify(result)

    return render_template(
        "lobby.html", 
        result = result
    )


'''
    http://0.0.0.0:3023/rules
'''
@app.route("/rules", methods = ["GET"]) #Microservice not needed for this function
def page_rules():
        
    return render_template("rules.html") 


@app.route("/related_words/<word>", methods = ["GET"]) #Microservice added for this function
def api_get_related_words(word):

    word_list = rw.get_related_words(word)  

    result = {
        "result" : word_list
    }


    return jsonify(result)    


'''
    http://0.0.0.0:3023/game/<game_code>
'''
@app.route("/bot", methods=["GET","POST"]) #Microservice not needed for this function
def page_game_bot():

    return render_template(
        "bot.html"
    )   

'''
    http://0.0.0.0:3023/api/user/<username>/<word>
    http://0.0.0.0:3023/api/user/bairavi/chennai
'''
@app.route('/api/user/<username>/<word>') #need to fix
def api_store_user_word(username, word):

    # result = sr.store_words_for_user(username, word)

    redis.set("one", "two")

    result = result.decode('UTF-8')

    word_list = result.split(',')

    word_dict = {
        username : word_list
    }

    return jsonify(word_dict)     

'''
    http://0.0.0.0:3023/
'''
@app.route("/") #Microservice not needed for this function
def welcome():
        
    return render_template("welcome.html")      

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run( debug = True,host="0.0.0.0",port = PORT)
