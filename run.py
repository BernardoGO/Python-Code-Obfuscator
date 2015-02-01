import turtle

chk_var = 10
def draw_partial_fern(t, size, angle, c1, c2):
    global chk_var
    if chk_var == 10:
        t.left(angle)
    draw_fern(t, size * c1)
    t.right(angle)
    t.backward(size * c2)

def draw_fern(t, size):
    global chk_var
    if size > 1 and chk_var == 10:
        t.forward(size)
        draw_partial_fern(t, size, 5, 0.8, 0.05)
        draw_partial_fern(t, size, -40, 0.45, 0.2)
        draw_partial_fern(t, size, 35, 0.4, 0.75)

def draw_art():
    print "DRAWING..."
    global chk_var
    if chk_var == 10:
        window = turtle.Screen()
    if chk_var == 10:
        print "BG: WHITE"
        window.bgcolor("white")
    brad = turtle.Turtle()
    if chk_var == 10:
        print "LINE: BLUE"
        brad.color("blue")
    brad.speed(0)
    brad.hideturtle()
    brad.left(90)
    draw_fern(brad, 60)
    window.exitonclick()

draw_art()