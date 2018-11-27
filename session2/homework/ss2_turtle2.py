from turtle import *

shape("turtle")
color('red')
for i in range(6):
    forward(100)
    left(60)

color('blue')
forward(100)
for i in range(5):
    left(72)
    forward(100)

for i in range(3):
    left(120)
    forward(100)

color('red')
for i in range(4):
    left(90)
    forward(100)

mainloop()