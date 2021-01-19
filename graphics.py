import turtle as trtl
hangman=trtl.Turtle()
hangman.ht()
# draw the blank lines, the spaces between them, and the letters for the word instructed
def display_word(word):
    print("TODO")

# erase the blank lines, any letters atop them, and any body parts or red letters drawn
def wipe_shown_word():
    hangman.clear()
    draw_hanger()

# draw the blank lines and the spaces between them for the word instructed
def setup_game(word):
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

# draws the part of the hangman representing the ith wrong guess, from zero
def draw_body_part(i):
    if i == 1:
        hangman.penup()
        hangman.goto(-100,100)
        hangman.pendown()
        hangman.circle(50)
    if i == 2:
        hangman.right(90)
        hangman.forward(30)
    if i == 3:
        hangman.right(30)
        hangman.forward(20)
    if i == 4:
        hangman.goto(-100,70)
        hangman.left(60)
        hangman.forward(20)
    if i == 5:
        hangman.penup()
        hangman.goto(-100,90)
        hangman.pendown()
        hangman.left(40)
        hangman.forward(20)
    if i == 6:
        hangman.goto(-100,90)
        hangman.right(130)
        hangman.forward(20)

# draws the letter with the other red, incorrect, used letters
def add_to_red_list(letter):
    hangman.penup()
    hangman.pencolor("red")
    hangman.setpos(-200/times_wrong, 0)
    hangman.write(letter)


# draws the letter on the space with the index requested
def fill_in_letter_at(i, letter):
    print("TODO")

# opens the interface and draws the initial picture, which is just a place to hang the man
def draw_hanger():
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