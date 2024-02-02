import subprocess
import sys
import turtle
import random
from config import Config

username = turtle.textinput("Boximus", "Enter Name:")
Config.username = username


# Big colorful squares pattern
turtle.bgcolor('black')
turtle.colormode(255)
turtle.speed(0)
turtle.tracer(0, 0)

for x in range(500):
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    turtle.pencolor(r, g, b)
    turtle.fd(x + 50)
    turtle.rt(91)

# Shadow
turtle.pencolor("white")
turtle.penup()
turtle.goto(-195, 157)
turtle.pendown()
turtle.write("Boximus", font=("Century Gothic", 72, "bold"))

# Setting background color and pen color
turtle.bgcolor("black")
turtle.pencolor("darkorange")
turtle.setup(width=800, height=600)
turtle.hideturtle()
turtle.speed("fastest")
turtle.tracer(0, 0)

# Set font size and style
turtle.penup()
turtle.goto(-200, 160)  # Adjust position as needed
turtle.pendown()
turtle.write("Boximus", font=("Century Gothic", 72, "bold"))

# Display username
penShadw = turtle.Turtle()
penShadw.color(204, 0, 255)
penShadw.penup()
penShadw.hideturtle()
penShadw.goto(2, -292)
penShadw.write("Player: {}".format(username), align="center", font=('San Francisco', 24, "bold"))

penU = turtle.Turtle()
penU.color(240, 179, 255)
penU.penup()
penU.hideturtle()
penU.goto(0, -290)
penU.write("Player: {}".format(username), align="center", font=('San Francisco', 24, "bold"))

# Setting up buttons


def play_button(x, y):
    # Define the coordinates of the button area
    button_x_min = -100
    button_x_max = 100
    button_y_min = -30
    button_y_max = 10

    return button_x_min <= x <= button_x_max and button_y_min <= y <= button_y_max


def exit_button(x, y):
    # Define the coordinates of the button area
    button_x_min = -100
    button_x_max = 100
    button_y_min = -110
    button_y_max = -70

    return button_x_min <= x <= button_x_max and button_y_min <= y <= button_y_max

selectDifficulty = "menutwo.py"

def on_screen_click(x, y):
    if play_button(x, y):
        print("Play")
        subprocess.run(f"python {selectDifficulty}", shell=True)

        print("Exiting program")
        sys.exit()

    elif exit_button(x, y):
        print("Bye Bye")
        turtle.bye()


# Create buttons
turtle.penup()
turtle.goto(2, -35)
turtle.pendown()
turtle.color(204, 102, 153)
turtle.write("PLAY", align="center", font=("San Francisco", 35, "bold"))
turtle.goto(0, -30)
turtle.pendown()
turtle.color("white")
turtle.write("PLAY", align="center", font=("San Francisco", 35, "bold"))

turtle.penup()
turtle.goto(2, -115)
turtle.pendown()
turtle.color(204, 102, 153)
turtle.write("EXIT", align="center", font=("San Francisco", 35, "bold"))
turtle.goto(0, -110)
turtle.pendown()
turtle.color("white")
turtle.write("EXIT", align="center", font=("San Francisco", 35, "bold"))

# Set up button click handling
turtle.onscreenclick(on_screen_click)

turtle.mainloop()
