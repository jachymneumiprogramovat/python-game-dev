import turtle as tt

GRID_SIZE = 450
FIELD_SIZE = GRID_SIZE // 3
RADIUS = (3 * FIELD_SIZE) // 4

pen = tt.Turtle()
screen = tt.Screen()


def draw_square(side_length):
    # Draw a square of side length 'side'.
    for _ in range(4):
        pen.forward(side_length)
        pen.left(90)


def draw_circle(x, y, radius):
    # Draw a circle of radius 'radius' at (x, y).
    pen.tiltangle(0)
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.circle(radius)


def draw_cross(x, y, radius):
    # Draw a cross centered at (x, y) of radius 'radius'.
    pen.penup()
    pen.goto(x - radius, y - radius)
    pen.pendown()
    pen.goto(x + radius, y + radius)
    pen.penup()
    pen.goto(x - radius, y + radius)
    pen.pendown()
    pen.goto(x + radius, y - radius)


def draw_grid(x, y, side_length):
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


def handle_click(x, y):
    pass


board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
screen.onclick(handle_click)

tt.mainloop()
