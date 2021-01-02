from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forward():
    # key "w"
    turtle.forward(10)


def move_backward():
    # key "s"
    turtle.backward(10)


def turn_clockwise():
    # key "d"
    turtle.right(10)


def turn_counter_clockwise():
    # key "a"
    turtle.left(10)


def clear_drawing():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
