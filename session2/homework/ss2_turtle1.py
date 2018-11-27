from turtle import *

shape("turtle")
color('red')
for i in range(2):
    left(60)
    forward(50)
left(60)
for i in range(2):
    left(60)
    forward(50)

for j in range(2):
    for i in range(2):
        forward(50)
        right(60)
    for i in range(2):    
        right(60)
        forward(50)
    right(30)
left(30)

for i in range(2):
    forward(50)
    left(60)
for i in range(2):
    left(60)
    forward(50)

mainloop()