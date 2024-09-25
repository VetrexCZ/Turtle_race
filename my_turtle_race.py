# Python Turtle race!

import turtle
from turtle import *
from random import randint

# Shutting down program
def ukoncit_program():
    turtle.bye()

# Window setup
turtle.Screen()

# Key shortcut for Shutting down program
turtle.listen()
turtle.onkey(ukoncit_program, "Escape")

# Turtle speed on max
speed(0)
penup()
goto(-140, 140)

# Racing track
for step in range(16):
    write(step, align ="center")
    right(90)

    # Draws the path
    for num in range(8):
        forward(10)
        pendown()
        forward(10)
        penup()

    backward(160)
    left(90)
    forward(20)

# Function for moving the turtles to the starting position
def priprav_hrace(turtle_obj, color, position):
    turtle_obj.color(color)
    turtle_obj.shape("turtle")
    turtle_obj.speed(3)
    turtle_obj.penup()
    turtle_obj.goto(-160, position)
    turtle_obj.pendown()

# Players setup
player_1 = Turtle()
priprav_hrace(player_1, "red", 100)

player_2 = Turtle()
priprav_hrace(player_2, "blue", 70)

player_3 = Turtle()
priprav_hrace(player_3, "green", 40)

player_4 = Turtle()
priprav_hrace(player_4, "orange", 10)


# turtles rotate 360°(Warm up)
for turn in range(10):
    player_1.right(36)

for turn in range(10):
    player_2.left(36)

for turn in range(10):
    player_3.right(36)

for turn in range(10):
    player_4.left(36)

# Finish line
finish_line = 144

# Function for first winner
def chceck_winner():
    if player_1.xcor() >= finish_line:
        return "Red", "red"
    elif player_2.xcor() >= finish_line:
        return "Blue", "blue"
    elif player_3.xcor() >= finish_line:
        return "Green", "green"
    elif player_4.xcor() >= finish_line:
        return "Orange", "orange"
    return None, None
    
# Random speed for turtles
winner = None
winner_color = None
while not winner: # Race continues until a winner is found
    player_1.forward(randint(1, 5))
    player_2.forward(randint(1, 5))
    player_3.forward(randint(1, 5))
    player_4.forward(randint(1, 5))
    # Checks, if some turtles reach the finish line
    winner,  winner_color = chceck_winner()

# Announcement of the win
penup()
goto(-110, -60) # L/R U/D
color(winner_color) # Set text color to the winners color
write(f"{winner} turtle wins!", font=("Arial", 20, "bold"))

# Keeps window open
turtle.done()