#Draw a sun:
import turtle
def draw_sun():
    turtle.speed(10)
    turtle.color("orange")
    for _ in range(36):
        turtle.forward(100)
        turtle.right(170)
draw_sun()
turtle.done()