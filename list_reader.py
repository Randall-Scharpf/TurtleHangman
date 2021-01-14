from random import random

# quickly a random word from the English list (normalized to difficulty by default once implemented)
def pick_random_word():
    listt = list(open('master word list.txt'))
    return listt[int(random()*len(listt))]