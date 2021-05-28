import requests
import json
import pprint
from bs4 import BeautifulSoup

def get_related_words(word):

    #print('Main')
    # Collect and parse first page

    page = requests.get('https://relatedwords.org/relatedto/' + str(word))

    soup = BeautifulSoup(page.text, 'lxml') 

    # print(soup)    

    items = soup.select('script')

    # item = items[items.length - 1]
    # print(item)
    item_list = ''
    # for item in items:
    #     i+=1
    content = str(items[7])
    a_string = content
    new_string = a_string.replace('<script id="preloadedDataEl" type="text/json">', "")
    new_string2 = new_string.replace('</script>',"")

    #print(new_string2)
    # item_list =  item_list + ',' +str(item.get_text())
    # print(item_list)
    content_json = json.loads(new_string2)
    #pprint.pprint(content_json)
    #print(content_json["query"])
    related_word_list = content_json["terms"]
    word_list = []
    for item in related_word_list[0:10]:
        if (' ' in item['word']):
            continue
        word_list.append(item['word'])

    return word_list

    


if __name__ == '__main__':
    related_words = get_related_words("yellow") 
    print(related_words)