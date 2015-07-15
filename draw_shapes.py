import turtle
t = turtle.Pen()
import sys

turtle.setup(650,620)
t.up()
t.setx(-300)
t.sety(260)
t.down()
t.speed(0)

def hello():
    print('Hey there! So you want to draw some shapes, eh?')
    print('What do you want to draw? Circles, squares, or triangles?')
    ans = sys.stdin.readline()
    ans = ans.strip()
    if ans == 'circles':
        import draw_circles
        draw_circles.t = t
        draw_circles.draw_circles()
    elif ans == 'squares':
        import draw_squares
        draw_squares.t = t
        draw_squares.draw_squares()
    elif ans == 'triangles':
        import draw_triangles
        draw_triangles.t = t
        draw_triangles.draw_triangles()

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