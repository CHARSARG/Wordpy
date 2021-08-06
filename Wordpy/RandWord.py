# Import the modules required
import json
from difflib import get_close_matches
import random


def randword():
    # Loading data from json file
    # in python dictionary
    data = json.load(open("words_dictionary.json"))

    allWords = list(data.items())
    #print(type(allWords))

    word=random.choice(allWords)
    #print(type(word))
    return(word[0])




#print(randword())
