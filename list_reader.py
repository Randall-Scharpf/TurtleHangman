'''
# quickly a random word from the English list (normalized to difficulty by default once implemented)
def pick_random_word():
    print ("TODO")
'''


# picks a random word from the master word list and output it in the console.
import random
word = (random.choice(list(open('master word list.txt'))))

print(word)
