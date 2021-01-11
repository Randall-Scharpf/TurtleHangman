import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()

x = -200
while (input("Continue? y/n") == "y"): 
  x = x + 50
  y = 200
  # begin added loop
  while (y > 0):
    y = y - 50
    painter.goto(x,y)
    painter.color("blue")
    painter.stamp()
  # end added loop
  painter.goto(x,y)
  painter.color("red")
  painter.stamp()