import random
from turtle import *

setup()
t1 = Turtle()
t1.up()

colors = ["blue", "red", "green", "yellow", "purple", "orange"]

t1.speed(0)


while True:
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    circle_size = random.randint(1,300)
    circle_color = random.choice(colors)

    t1.goto(x,y)
    
    t1.down()
    t1.color(circle_color)
    t1.circle(circle_size)
    t1.up()
