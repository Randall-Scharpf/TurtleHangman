#there is error somewhere
#this is code for letter lines
import turtle as trtl
hangman=trtl.Turtle()
#put these values just to make sure code works. can just delete
value = 9
word = "pigs back"
hangman.penup()
hangman.goto(-15*value,-150)
hangman.seth(0)
letters = list(word)
for letter in letters:
    if letter == (" "):
        hangman.penup()
        hangman.forward(30)
    else:
        hangman.penup()
        hangman.forward(10)
        hangman.pendown()
        hangman.forward(20)