from turtle import Turtle, Screen
from prettytable import PrettyTable
import pyjokes

joke = pyjokes.get_joke('en', 'neutral')
# print(joke)


# timmy = Turtle()
# my_screen = Screen()
# my_screen.canvheight
# print(my_screen)
# my_screen.exitonclick()

# timmy.shape("turtle") # This
# timmy.color("coral")  # does not
# timmy.forward(100)    # work for some reason

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"
print(table)
