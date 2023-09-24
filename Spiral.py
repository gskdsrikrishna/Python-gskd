#Draw a spiral:
import turtle
def draw_spiral():
    length = 5
    angle = 90
    for _ in range(40):
        turtle.forward(length)
        turtle.right(angle)
        length += 5
draw_spiral()
turtle.done()