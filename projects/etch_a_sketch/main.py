from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forward():
    # key "w"
    turtle.forward(10)


def move_backward():
    # key "s"
    pass


def move_clockwise():
    # key "d"
    pass


def move_counter_clockwise():
    # key "a"
    pass


def clear_screen():
    screen.clearscreen()


screen.listen()
screen.onkey(key="w", fun=move_forward)

screen.exitonclick()