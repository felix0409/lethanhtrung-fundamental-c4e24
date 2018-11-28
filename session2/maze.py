from turtle import *

d = 0
shape("turtle")
for i in range(50):
    forward(d)
    left(90)
    d += 10

mainloop()