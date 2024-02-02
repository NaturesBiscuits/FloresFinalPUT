import sys
import turtle
import random
import subprocess
from config import Config

# Big colorful squares pattern
turtle.bgcolor('black')
turtle.colormode(255)
turtle.speed(0)
turtle.tracer(0, 0)

for x in range(500):
    r, b, g = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

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
penShadw.write("Player: {}".format(Config.username), align="center", font=('San Francisco', 24, "bold"))

penU = turtle.Turtle()
penU.color(240, 179, 255)
penU.penup()
penU.hideturtle()
penU.goto(0, -290)
penU.write("Player: {}".format(Config.username), align="center", font=('San Francisco', 24, "bold"))


# Setting up buttons
def easy_button(x, y):
    button_x_min = -100
    button_x_max = 100
    button_y_min = -30
    button_y_max = 10

    return button_x_min <= x <= button_x_max and button_y_min <= y <= button_y_max

def medium_button(x, y):
    # Define the coordinates of the button area
    button_x_min = -100
    button_x_max = 100
    button_y_min = -110
    button_y_max = -70

    return button_x_min <= x <= button_x_max and button_y_min <= y <= button_y_max

def hard_button(x, y):
    # Define the coordinates of the hard button area
    button_x_min = -100
    button_x_max = 100
    button_y_min = -190  # Positioned below medium button
    button_y_max = -150
    return button_x_min <= x <= button_x_max and button_y_min <= y <= button_y_max


game_pyfile = "boximus.py"

def on_screen_click(x, y):
    global speed  # Declare the variable as global to modify the outer variable

    if easy_button(x, y):
        print("Easy")
        Config.speed = 0.2
    elif medium_button(x, y):
        print("Medium")
        Config.speed = 0.3
    elif hard_button(x, y):
        print("Hard")
        Config.speed = 0.5

    # Start the game with the selected speed
    subprocess.run(f"python {game_pyfile}", shell=True)
    sys.exit()

def on_screen_click(x, y):
    if easy_button(x, y):
        print("Easy")
        subprocess.run(f"python {game_pyfile}", shell=True)
        sys.exit()

    elif medium_button(x, y):
        print("Medium")
        subprocess.run(f"python {game_pyfile}", shell=True)
        sys.exit()

    elif hard_button(x, y):
        print("Hard")
        subprocess.run(f"python {game_pyfile}", shell=True)
        sys.exit()

# Create buttons
turtle.penup()
turtle.goto(2, -35)
turtle.pendown()
turtle.color(204, 102, 153)
turtle.write("EASY", align="center", font=("San Francisco", 35, "bold"))
turtle.goto(0, -30)
turtle.pendown()
turtle.color("white")
turtle.write("EASY", align="center", font=("San Francisco", 35, "bold"))

turtle.penup()
turtle.goto(2, -115)
turtle.pendown()
turtle.color(204, 102, 153)
turtle.write("MEDIUM", align="center", font=("San Francisco", 35, "bold"))
turtle.goto(0, -110)
turtle.pendown()
turtle.color("white")
turtle.write("MEDIUM", align="center", font=("San Francisco", 35, "bold"))

turtle.penup()
turtle.goto(2, -195)
turtle.pendown()
turtle.color(204, 102, 153)
turtle.write("HARD", align="center", font=("San Francisco", 35, "bold"))
turtle.goto(0, -190)
turtle.pendown()
turtle.color("white")
turtle.write("HARD", align="center", font=("San Francisco", 35, "bold"))

# Set up button click handling
turtle.onscreenclick(on_screen_click)

turtle.mainloop()
