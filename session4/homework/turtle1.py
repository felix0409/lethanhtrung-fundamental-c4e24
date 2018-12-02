from turtle import *

shape("turtle")
speed(200)
color('light blue')
for i in range(7):
    forward(100)
    left(360/7)

color('yellow')
forward(100)
for i in range(6):
    left(60)
    forward(100)

color('brown')
for i in range(5):
    left(72)
    forward(100)

color('blue')
for i in range(4):
    left(90)
    forward(100)

color('red')
for i in range(3):
    left(120)
    forward(100)
mainloop()