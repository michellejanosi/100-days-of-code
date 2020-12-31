from turtle import Turtle, Screen, color
import random
# import colorgram

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     rgb_colors.append((r, g, b))

# print(rgb_colors)
color_list = [(131, 164, 204), (228, 149, 99), (30, 44, 64), (238, 245, 242), (245, 234, 238), (166, 58, 48), (202, 135, 147), (237, 212, 85), (41, 101, 150), (135, 183, 161), (150, 62, 71), (52, 42, 45), (159, 33, 31), (219, 82, 73), (238, 165, 155), (58, 117, 99), (60, 49, 45), (173, 29, 31), (231, 163, 168), (35, 61, 56), (15, 96, 71), (33, 60, 107), (170, 188, 222), (188, 101, 111), (104, 126, 161), (14, 85, 109), (174, 200, 188), (33, 151, 211)]

# 10 x 10 in size, dots are sized at 20, 50 paces apart
turtle = Turtle()
screen = Screen()

screen.colormode(255)
screen.screensize(150, 150)
screen.bgcolor("#F6F6F6")
turtle.speed("fastest")
turtle.penup()
turtle.ht()  
pos_x = -290
pos_y = -230
num_lines = 100

while num_lines > 0:
    turtle.setpos(pos_x, pos_y)

    for _ in range(10):
        turtle.fd(10)
        turtle.dot(20, random.choice(color_list))
        turtle.fd(50)
        pos_y += 5
        num_lines -= 1

screen.exitonclick()
