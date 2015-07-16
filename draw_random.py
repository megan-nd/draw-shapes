import sys
import random
t = None

def triangle():
    side_length = random.randint(5,50)
    for x in range(1,4):
        t.forward(side_length)
        t.left(360/3)
    t.up()
    t.forward(side_length+10)
    t.down()

def circle():
    radius = random.randint(5,18)
    t.circle(radius)
    t.up()
    t.forward(radius*2+5)
    t.down()

def square():
    side_length = random.randint(5,50)
    for x in range(1,5):
        t.forward(side_length)
        t.left(90)
    t.up()
    t.forward(side_length+10)
    t.down()

def draw_random():
    quantity = random.randint(1,16)
    ans = random.choice([circle,square,triangle])
    if ans == circle():
        radius = random.randint(5,18)
        for x in range (1,quantity):
            circle()
    elif ans == square():
        side_length = random.randint(5,50)
        for x in range (1,quantity):
            square()
    elif ans == triangle():
        side_length = random.randint(5,50)
        for x in range (1,quantity):
            triangle()
