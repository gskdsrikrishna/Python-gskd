#Draw a snowflake:
import turtle
def draw_snowflake():
    for _ in range(6):
        turtle.forward(100)
        turtle.backward(50)
        turtle.right(60)
        turtle.forward(50)
        turtle.backward(100)
        turtle.right(60)
draw_snowflake()
turtle.done()