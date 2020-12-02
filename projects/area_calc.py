# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 6 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height ✖️ wall width) ÷ coverage per can.
import math 

height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
coverage = 6

def paint_area_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")


paint_area_calc(height=height, width=width, cover=coverage)