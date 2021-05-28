import spacy
from spacy.lang.en import English
from spacy.matcher import Matcher
def similarity(c1,c2):
    nlp=spacy.load("en_core_web_sm")

    c1=nlp("current word")

    c2=nlp("previous word")

    val=(c1.similarity(c2))

    print(val)

if __name__ == "__main__":
    similarity()
