from turtle import Turtle, Screen, shape
import random
# from prettytable import PrettyTable
# import pyjokes

# joke = pyjokes.get_joke('en', 'neutral')
# print(joke)


# timmy = Turtle()
# my_screen = Screen()
# my_screen.canvheight
# print(my_screen)
# my_screen.exitonclick()

# timmy.shape("turtle") # This
# timmy.color("coral")  # does not
# timmy.forward(100)    # work for some reason

# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Fire", "Water"])
# table.align = "l"
# print(table)

turtle = Turtle()
screen = Screen()
# turtle.color("DeepSkyBlue")
screen.colormode(255)
turtle.pensize(10)
turtle.speed("fast")

# draw a square
# for _ in range(4):
#     turtle.forward(100)
#     turtle.left(90) 

# draw a dashed line
# for _ in range(15):
#     turtle.fd(10)
#     turtle.penup()
#     turtle.fd(10)
#     turtle.pendown()

# draw random geometric shapes in random colors
# num_sides = 5

# colours = ["crimson", "dark orange", "gold",
#           "medium spring green", "green", "deep sky blue", "medium blue", "magenta", "medium purple", "dark slate blue"]

# return a random color for the turtle pen color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

# def draw_shape(num_sides):
#     angle = 360 / num_sides  
#     for _ in range(num_sides):
#         turtle.fd(100)
#         turtle.right(angle)

# for shape_side_n in range(3, 11):
#     turtle.color(random.choice(colours))
#     draw_shape(shape_side_n)

# turtle random walk
# directions = [0, 90, 180, 270]
# for _ in range(200):
#     turtle.forward(30)
#     turtle.color(random_color())
#     turtle.setheading(random.choice(directions))

# draw a spirograph


screen.exitonclick()
