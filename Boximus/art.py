import turtle
from itertools import cycle
window = turtle.Screen()
window.title("Boxumus")
window.bgcolor("black")
window.setup(width=800, height=600)

ANGLE = 8

colorspiral = ["orange", "tan", "pink", "coral"]

def spiral(turtle, radius, color_names):
    colorspiral = cycle(color_names)

    for _ in range(360 // ANGLE):
        turtle.color(next(colorspiral))
        turtle.circle(radius)
        turtle.left(ANGLE)
        turtle.pensize(0.5)


redBox = turtle.Turtle()
redBox.hideturtle()
redBox.goto(0, -75)

redColors = ['red', 'dark red']
for number in range(400):
    redBox.forward(number+1)
    redBox.right(89)
    redBox.pencolor(redColors[number % 2])
redBox.speed("fastest")

yertle = Turtle(visible=False)
yertle.speed("fastest")
spiral(turtle, 400, colorspiral)

window.exitonclick()
