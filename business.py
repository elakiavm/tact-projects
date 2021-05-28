'''
Source:

Author: Serkinti Team
    Sharon
    TODO: add other team members
'''
import requests
import os
import json

API_URL = os.environ.get('API_URL')

def get_word_score_ms_api(word) :

    serkinti_url =  API_URL + '/api/get/word/score?word='+str(word)

    print('serkinti_url: ', serkinti_url)
    
    result = requests.get(serkinti_url)

    print(result)
    print(result.content)

    resp_json = json.loads(result.content)

    # return resp_json['reversed_name']

    return resp_json