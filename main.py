import turtle as trtl
hangman=trtl.Turtle()
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
#too lazy to do eyes for now
wn = trtl.Screen()
wn.mainloop()

