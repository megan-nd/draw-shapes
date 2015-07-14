import turtle
t = turtle.Pen()
import sys

side_length = 0

def triangle():
    for x in range(1,4):
        t.forward(side_length)
        t.left(360/3)
    t.up()
    t.forward(side_length+10)
    t.down()

def topcorner():
    t.up()
    t.backward(250)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.down()

def draw_triangles():
    global side_length
    print('How many triangles do you want?')
    ans = int(sys.stdin.readline())
    if ans <= 10:
        print('How big?')
        ans2 = int(sys.stdin.readline())
        side_length = ans2
        if side_length <= 50:
            for x in range(1,ans+1):
                triangle()
        else:
            print('That\'s too big')
            return
    else:
        print('Ok! Here we go!')
        side_length = 30
        for x in range(1,ans+1):
            triangle()

def draw_again():
    t.up()
    t.backward(ans*(side_length+10))
    t.right(90)
    t.forward(50)
    t.left(90)
    t.down()

def again():
    while True:
        print('Press enter to draw again')
        input()
        draw_again()
        draw_triangles() 

topcorner()
draw_triangles()
again()
