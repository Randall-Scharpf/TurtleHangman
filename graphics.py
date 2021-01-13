# draw the blank lines, the spaces between them, and the letters for the word instructed
def display_word(word):
    print("TODO")

# erase the blank lines, any letters atop them, and any body parts or red letters drawn
def wipe_shown_word():
    print("TODO")

# draw the blank lines and the spaces between them for the word instructed
def setup_game(word):
    print("TODO")

# draws the part of the hangman representing the ith wrong guess, from zero
def draw_body_part(i):
    print("TODO")

# draws the letter with the other red, incorrect, used letters
def add_to_red_list(letter):
    print("TODO")

# draws the letter on the space with the index requested
def fill_in_letter_at(i, letter):
    print("TODO")

# opens the interface and draws the initial picture, which is just a place to hang the man
def draw_hanger():
    print("TODO")

import turtle as trtl
hangman=trtl.Turtle()
hangman.ht()
times_wrong=1
if times_wrong == 1:
    hangman.penup()
    hangman.goto(-100,100)
    hangman.pendown()
    hangman.circle(50)
    times_wrong+=1
if times_wrong == 2:
    hangman.right(90)
    hangman.forward(30)
    times_wrong+=1
if times_wrong == 3:
    hangman.right(30)
    hangman.forward(20)
    times_wrong+=1
if times_wrong == 4:
    hangman.goto(-100,70)
    hangman.left(60)
    hangman.forward(20)
    times_wrong+=1
if times_wrong == 5:
    hangman.penup()
    hangman.goto(-100,90)
    hangman.pendown()
    hangman.left(40)
    hangman.forward(20)
    times_wrong+=1
if times_wrong == 6:
    hangman.goto(-100,90)
    hangman.right(130)
    hangman.forward(20)
#draws the hanger
hangman.penup()
hangman.setpos(-150,0)
hangman.pendown()
hangman.seth(0)
hangman.forward(200)
hangman.setpos(0,0)
hangman.seth(90)
hangman.forward(250)
hangman.seth(180)
hangman.forward(100)
hangman.seth(270)
hangman.forward(50)

#too lazy to do eyes for now
wn = trtl.Screen()
wn.mainloop()
