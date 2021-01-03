from turtle import Turtle, Screen, shape
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_coord = [-70, -40, -10, 20, 50, 80]
turtles = []
is_race_on = False

for turtle_index in range(0, 6):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=y_coord[turtle_index])
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        

screen.exitonclick()
