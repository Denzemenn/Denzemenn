#  import random
# import random as r
#  from random import randint
#  from random import
# x = r.randint(0, 100)
# lst = [0, 1, 2, 3, 4, 5]
# element_random = r.choice(lst)
# r.shuffle(lst)
#
# print(x)
# print(lst)
# print(element_random)

import turtle as t
t.shape("turtle")
t.penup()
t.goto(-300, 250)
t.pendown()
screen = t.Screen()
t.color("black", "yellow")
t.pensize(5)
t.speed(0)

hor = 300
vert = 200
t.begin_fill()
t.forward(hor)
t.right(90)
t.forward(vert)
t.right(90)
t.forward(hor)
t.right(90)
t.forward(vert)
t.right(90)
t.end_fill()

t.penup()
t.goto(-100,200)
t.pendown()
t.pensize(7)
t.fd(75)

t.write("Movavi", font=("Arial Black", 50, "normal"), align="center")


screen.exitonclick()