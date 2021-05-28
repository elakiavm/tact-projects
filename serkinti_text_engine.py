import random
import spacy
#import similarity as sim
#import word_similarity as ws
import word_store as wsj
import related_words as rw

def get_rare_words():

    with open('gre_words.txt') as f:
        lines = [line.rstrip() for line in f]

    return lines

def get_word_score(word, game_code, player_index):

    # if word has more than 4 letters, high scoring probability
    # if(len(word) > 3):
        # score_probability += 20

    score_probability = len_score(len(word))

    score_probability = vowels(score_probability, word)

    # similarity_score  = ws.get_word_similarity(word, "game")

    #print(similarity_score)

    score = random.randint(score_probability, (score_probability+10))

    wsj.store_word(word, score, game_code, player_index)

    #score_probability = score_probability/20

    #print(f'[ste] word: {word}, score : {score}')

    return score

def len_score(word_length):

    if(word_length < 1):
        return 0

    if(word_length < 4):
        return 20

    if(word_length < 8):
        return 30

    if(word_length < 10):
        return 50

    return 90       

def vowels(score_probability, word):

    word        = word.lower()
    
    raw_word    = word
    vowels      = 0

    for i in raw_word:
      if(
          i == 'a' 
          or i == 'e' 
          or i == 'i' 
          or i == 'o' 
          or i == 'u' 
        ):
            vowels = vowels + 1

    if(vowels > 3):
        score_probability += 20   

    return score_probability    


def startpy():

    print("s")

if __name__ == "__main__":
    startpy()
    