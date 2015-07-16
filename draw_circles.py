import sys
t = None

def circle(radius):
    t.circle(radius)
    t.up()
    t.forward(radius*2+5)
    t.down()

def draw_circles():
    fixed_radius = 18
    print('How many circles do you want?')
    ans = int(sys.stdin.readline())
    if ans <= 10:
        print('How big?')
        ans2 = int(sys.stdin.readline())
        radius = ans2
        if radius <= 30:  #px
            for x in range(1,ans+1):
                circle(radius)
        else:
            print('That\'s too big')
            return
    elif ans >= 11 and ans <=15:  #can fit 15 in a row
        print('Ok! Here we go!')
        for x in range(1,ans+1):
            circle(fixed_radius)
    elif ans >= 16 and ans <=30:
        print('Ok! Here we go!')
        for x in range(1,16):
            circle(fixed_radius)
        draw_again()
        for x in range(1,(ans-15)+1):
            circle(fixed_radius)
    elif ans >= 31:
        print('Wow.. that\'s a lot.. but ok!')
        for x in range(1,(int(ans/15+1))):
            one_row(fixed_radius)
            draw_again()
        for x in range(1,(ans-(15*(int(ans/15)))+1)):
            circle(fixed_radius)
        print(ans-(15*(int(ans/15)))+1)
    elif ans > 180:
        print('This canvas isn\'t big enough for that.. sorry')
        return

def one_row(radius):
    for x in range(1,16):
        circle(radius)

def draw_again():
    t.up()
    t.setx(-300)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.down()
