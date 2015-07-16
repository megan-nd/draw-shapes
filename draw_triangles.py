import sys
t = None

side_length = 0

def triangle():
    for x in range(1,4):
        t.forward(side_length)
        t.left(360/3)
    t.up()
    t.forward(side_length+10)
    t.down()

def draw_triangles():
    global side_length
    print('How many triangles do you want?')
    ans = int(sys.stdin.readline())
    if ans <= 10:
        print('How big?')
        ans2 = int(sys.stdin.readline())
        side_length = ans2
        if side_length <= 50:  #px
            for x in range(1,ans+1):
                triangle()
        else:
            print('That\'s too big')
            return
    elif ans >= 11 and ans <=15:  #can fit 15 in a row
        print('Ok! Here we go!')
        side_length = 30
        for x in range(1,ans+1):
            triangle()
    elif ans >= 16 and ans <=30:
        print('Ok! Here we go!')
        side_length = 30
        for x in range(1,16):
            triangle()
        draw_again()
        for x in range(1,(ans-15)+1):
            triangle()
    elif ans >= 31:
        print('Wow.. that\'s a lot.. but ok!')
        side_length = 30
        for x in range(1,(int(ans/15+1))):
            one_row()
            draw_again()
        for x in range(1,(ans-(15*(int(ans/15)))+1)):
            triangle()
        print(ans-(15*(int(ans/15)))+1)
    elif ans > 180:
        print('This canvas isn\'t big enough for that.. sorry')
        return

def one_row():
    for x in range(1,16):
        triangle()

def draw_again():
    t.up()
    t.setx(-300)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.down()
