import turtle
import math
def drawCircle(x,y,radius):
    t = turtle.Turtle()
    s = turtle.Screen()

    t.penup()
    t.goto(x,y)
    t.setheading(180)
    t.setheading(-1)
    t.goto(x , y-radius)
    t.pendown()
    for turn in range(120):
        t.left(3)
        t.forward(2.0 * math.pi * radius / 120)

    s.exitonclick()

drawCircle(50,75,100)
