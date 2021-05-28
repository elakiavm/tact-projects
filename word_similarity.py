
'''
Created on 
Course work: 
@author: Vedha
Source:
    https://stackoverflow.com/questions/65852710/text-similarity-using-word2vec 
    https://stackoverflow.com/questions/14463277/how-to-disable-python-warnings 
    https://relatedwords.org/
    https://relatedwords.org/relatedto/yellow
    https://relatedwords.org/relatedto/energy
pip:
    gensim
    python-Levenshtein
'''

# Import necessary modules
from scipy import spatial
import gensim.downloader as api
import numpy as np

import warnings

warnings.filterwarnings("ignore")

model = api.load("glove-wiki-gigaword-50") #choose from multiple models https://github.com/RaRe-Technologies/gensim-data

def preprocess(s):
    return [i.lower() for i in s.split()]

def get_vector(s):
    return np.sum(np.array([model[i] for i in preprocess(s)]), axis=0)

def test_base():

    s0 = 'Mark zuckerberg owns the facebook company'
    s1 = 'Facebook company ceo is mark zuckerberg'
    s2 = 'Microsoft is owned by Bill gates'
    s3 = 'How to learn japanese'

    print('s0 vs s1 ->',)
    print('s0 vs s2 ->', 1 - spatial.distance.cosine(get_vector(s0), get_vector(s2)))
    print('s0 vs s3 ->', 1 - spatial.distance.cosine(get_vector(s0), get_vector(s3)))

word_list = [
    "friend",
    "comrade",
    "companion"
]

def get_word_similarity(word1, word2):

    sim = (1 - spatial.distance.cosine(get_vector(word1), get_vector(word2)))

    return sim

def startpy():

    compare_list = [
        ["friend", "comrade"],
        ["energy", "force"],
        ["energy", "power"],
        ["pen", "pencil"],
        ["water", "bottle"]
    ]

    for sub_list in compare_list:

        # print(sub_list)

        word1 = sub_list[0]
        word2 = sub_list[1]

        sim = get_word_similarity(word1, word2)

        result = f"{word1}, {word2}, {sim}"

        print(result)

if __name__ == '__main__':
    startpy()