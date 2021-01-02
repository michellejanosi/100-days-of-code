from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)


def move_backward():
    pass


def move_clockwise():
    pass


def move_counter_clockwise():
    pass


def clear_screen():
    pass


screen.listen()
screen.onkey(key="w", fun=move_forward)

screen.exitonclick()