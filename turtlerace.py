from turtle import *
import random

screen = Screen()
screen.title("Turtle Racing")
screen.bgpic(
    "workspace/Turtle/bgpic.gif")
screen.setup(width=500, height=350)

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# Make turtle objects, moving them to the starting point
# Each turtles gets y += 40
y = -100
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y)
    all_turtles.append(new_turtle)
    y += 40

race = False
if user_bet:
    race = True

while race:
    for turtle in all_turtles:
        if turtle.pos()[0] >= 215:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {winning_color} turtle is the winner!")
            race = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
