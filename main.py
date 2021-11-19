import turtle as tt

HraciPole = 600
Policko = HraciPole // 3
poloměr = (3 * Policko) // 8
hranice = HraciPole // 2

pen = tt.Turtle()
screen = tt.Screen()


def ctverec(side_length):
    # Draw a square of side length 'side'.
    for _ in range(4):
        pen.forward(side_length)
        pen.left(90)


def kolecko(x, y, radius):
    # Draw a circle of radius 'radius' at (x, y).
    pen.tiltangle(0)
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.circle(radius)


def krizek(x, y, radius):
    # Draw a cross centered at (x, y) of radius 'radius'.
    pen.penup()
    pen.goto(x - radius, y - radius)
    pen.pendown()
    pen.goto(x + radius, y + radius)
    pen.penup()
    pen.goto(x - radius, y + radius)
    pen.pendown()
    pen.goto(x + radius, y - radius)


def tabulka(x, y, side_length):
    third = side_length // 3
    pen.pu()
    pen.goto(x, y)

    for i in range(4):
        pen.pd()
        pen.goto(x + i * third, y + side_length)
        pen.pu()
        pen.goto(x + (i + 1) * third, y)

    pen.pu()
    pen.goto(x, y)
    for i in range(4):
        pen.pd()
        pen.goto(x + side_length, y + i * third)
        pen.pu()
        pen.goto(x, y + (i + 1) * third)


def kliknuti(x, y):
    global player, pole
    if abs(x) <= hranice and abs(y) <= hranice:
        row = (-int(y) + hranice) // Policko
        col = (int(x) + hranice) // Policko

        if pole[row][col]==0:
            pole[row][col] = player
        else:
            print("tí")
            return

        center = (
            -hranice + col * Policko + Policko // 2,
            hranice - row * Policko - Policko // 2
        )

        if player == 1:
            krizek(center[0], center[1], poloměr)
        else:
            kolecko(center[0], center[1], poloměr)
        kdovyhral()
        player = -player


def kdovyhral():
    for i in pole:
        if abs(sum(i))==3:
            print("vyhral")
    for i in range(3):
        if abs(pole[0][i]+pole[1][i]+pole[2][i])==3 :
            print("vyhral")
    
    if abs(pole[0][0]+pole[1][1]+pole[2][2])==3:
        print("vyhral")
    
    if abs(pole[0][2]+pole[1][1]+pole[2][0])==3:
        print("vyhral")
pole = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
player = 1
screen.onclick(kliknuti)
pen.speed(100)
pen.hideturtle()

tabulka(-hranice, -hranice, HraciPole)

tt.mainloop()
