import turtle as trtl
writer=trtl.Turtle()
writer.ht()

# draw the blank lines, the spaces between them, and the letters for the word instructed
def display_word(word):
    letters = list(word)
    length=len(word)
    for i in letters:
        writer.pencolor("black")
        writer.penup()
        writer.setpos(-15*length, -150)
        writer.pendown()
        writer.write(i)

# erase the blank lines, any letters atop them, and any body parts or red letters drawn
def wipe_shown_word():
    writer.clear()
    writer.clear()
    draw_hanger()

times_wrong = 0

# draw the blank lines and the spaces between them for the word instructed
def setup_game(word):
    global times_wrong
    times_wrong = 0
    writer.penup()
    writer.goto(-15 * len(word) - 5,-150)
    writer.seth(0)
    letters = list(word)
    i = 0
    for letter in letters:
        if i + 1 == len(word):
            return
        if not letter.isalpha():
            writer.penup()
            writer.forward(30)
            fill_in_letter_at(i, letter)
        else:
            writer.pendown()
            writer.forward(20)
        i = i + 1

# draws the part of the writer representing the ith wrong guess, from zero
def draw_body_part(i):
    if i == 1:
        writer.penup()
        writer.goto(-100,100)
        writer.pendown()
        writer.circle(50)
    if i == 2:
        writer.right(90)
        writer.forward(30)
    if i == 3:
        writer.right(30)
        writer.forward(20)
    if i == 4:
        writer.goto(-100,70)
        writer.left(60)
        writer.forward(20)
    if i == 5:
        writer.penup()
        writer.goto(-100,90)
        writer.pendown()
        writer.left(40)
        writer.forward(20)
    if i == 6:
        writer.goto(-100,90)
        writer.right(130)
        writer.forward(20)

# draws the letter with the other red, incorrect, used letters
def add_to_red_list(letter):
    global times_wrong
    times_wrong = times_wrong + 1
    writer.penup()
    writer.pencolor("red")
    writer.setpos(-200 * (times_wrong - 1), 0)
    writer.write(letter)

# draws the letter on the space with the index requested
def fill_in_letter_at(i, letter):
    print("TODO")

# opens the interface and draws the initial picture, which is just a place to hang the man
def draw_hanger():
    writer.penup()
    writer.setpos(-150,0)
    writer.pendown()
    writer.seth(0)
    writer.forward(200)
    writer.setpos(0,0)
    writer.seth(90)
    writer.forward(250)
    writer.seth(180)
    writer.forward(100)
    writer.seth(270)
    writer.forward(50)