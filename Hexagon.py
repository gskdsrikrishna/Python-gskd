#Draw a hexagon:
import turtle
def draw_hexagon():
    for _ in range(6):
        turtle.forward(100)
        turtle.right(60)
draw_hexagon()
turtle.done()