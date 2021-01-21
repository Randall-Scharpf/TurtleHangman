import turtle as trtl
writer=trtl.Turtle()
hangman=trtl.Turtle()
writer.ht()
hangman.ht()
writer.pensize(5)
hangman.pensize(5)
style = ('Arial', 20, 'bold')
# draw the blank lines, the spaces between them, and the letters for the word instructed
def display_word(word):
    setup_game(word)
    writer.pencolor("black")
    i = 0
    for letter in word.upper():
        writer.penup()
        writer.setpos((-15*len(word))+(i*30) + 5 , -145)
        writer.pendown()
        writer.write(letter, font=style, align='center')
        i = i + 1

# erase the blank lines, any letters atop them, and any body parts or red letters drawn
def wipe_shown_word():
    writer.clear()
    hangman.clear()
    draw_hanger()

times_wrong = 0

# draw the blank lines and the spaces between them for the word instructed
def setup_game(word):
    global times_wrong
    times_wrong = 0
    writer.pencolor("black")
    writer.penup()
    writer.goto(-15 * len(word) - 5,-145)
    writer.seth(0)
    letters = list(word)
    i = 0
    for letter in letters:
        if i == len(word):
            return
        if not letter.isalpha():
            fill_in_letter_at(i, letter, word)
            writer.penup()
            writer.goto((-15 * len(word) - 5 + 30*i),-145)
            writer.forward(30)
        else:
            writer.pendown()
            writer.forward(20)
            writer.penup()
            writer.forward(10)
        i = i + 1

# draws the part of the writer representing the ith wrong guess, from zero
def draw_body_part(i):
    if i == 0:
        hangman.seth(0)
        hangman.penup()
        hangman.goto(-100,100)
        hangman.pendown()
        hangman.circle(20)
    if i == 1:
        hangman.right(90)
        hangman.forward(30)
    if i == 2:
        hangman.right(30)
        hangman.forward(20)
    if i == 3:
        hangman.goto(-100,70)
        hangman.left(60)
        hangman.forward(20)
    if i == 4:
        hangman.penup()
        hangman.goto(-100,90)
        hangman.pendown()
        hangman.left(40)
        hangman.forward(20)
    if i == 5:
        hangman.goto(-100,90)
        hangman.right(130)
        hangman.forward(20)
    if i == 6:
        hangman.penup()
        hangman.goto(-90, 120)
        hangman.pendown()
        hangman.seth(90)
        hangman.circle(2)

        hangman.penup()
        hangman.goto(-110,120)
        hangman.pendown()
        hangman.seth(270)
        hangman.circle(2)
    if i == 7:
        hangman.penup()
        hangman.goto(-105,110)
        hangman.pendown()
        hangman.seth(0)
        hangman.forward(10)

# draws the letter with the other red, incorrect, used letters
def add_to_red_list(letter):
    global times_wrong
    times_wrong = times_wrong + 1
    writer.penup()
    writer.pencolor("red")
    writer.setpos(-200 + 30*(times_wrong), 190)
    writer.write(letter, font=style, align='center')

# draws the letter on the space with the index requested
def fill_in_letter_at(i, letter, word):
    writer.penup()
    writer.goto(((-15*len(word)) + i*30 + 5) ,-145)
    writer.pendown()
    writer.pencolor("black")
    writer.write(letter, font=style, align='center')

# opens the interface and draws the initial picture, which is just a place to hang the man
def draw_hanger():
    hangman.pencolor("black")
    hangman.penup()
    hangman.setpos(-150,0)
    hangman.pendown()
    hangman.seth(0)
    hangman.forward(200)
    hangman.setpos(0,0)
    hangman.seth(90)
    hangman.forward(170)
    hangman.seth(180)
    hangman.forward(100)
    hangman.seth(270)
    hangman.forward(30)