#Draw a flower:
import turtle
def draw_flower():
    turtle.color("red")
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for _ in range(36):
        turtle.forward(100)
        turtle.left(170)
    turtle.end_fill()
draw_flower()
turtle.done()