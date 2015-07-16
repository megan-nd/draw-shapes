import turtle
t = turtle.Pen()
import sys
import random

import draw_circles, draw_squares, draw_triangles, draw_random

draw_circles.t = t
draw_squares.t = t
draw_triangles.t = t
draw_random.t = t

turtle.setup(650,620)
t.up()
t.setx(-300)
t.sety(260)
t.down()
t.speed(0)

print('Hey there! So you want to draw some shapes, eh?')

def hello():
    print('What do you want to draw? Circles, squares, triangles.. or let me pick?')
    ans = sys.stdin.readline()
    ans = ans.strip()
    if ans == 'circles':
        draw_circles.draw_circles()
    elif ans == 'squares':
        draw_squares.draw_squares()
    elif ans == 'triangles':
        draw_triangles.draw_triangles()
    elif ans == 'you pick':
        print('Yay!')
        draw_random.draw_random()

def draw_again():
    t.up()
    t.setx(-300)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.down()

def again():
    while True:
        print('Press enter to draw again')
        input()
        draw_again()
        hello()

hello()
again()
