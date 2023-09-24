#Analog Clock:

import turtle
import datetime

# Set up the turtle
window = turtle.Screen()
window.bgcolor("white")
window.title("Analog Clock")
window.setup(width=600, height=600)
window.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)


def draw_clock(h, m, s):
    # Draw clock face
    pen.up()
    pen.goto(0, -200)
    pen.setheading(90)
    pen.color("black")
    pen.pendown()
    pen.circle(200)

    # Draw hour hand
    pen.up()
    pen.goto(0, 0)
    pen.color("black")
    pen.setheading(90)
    angle = (h / 12) * 360 + (m / 60) * 30
    pen.right(angle)
    pen.pendown()
    pen.forward(100)

    # Draw minute hand
    pen.up()
    pen.goto(0, 0)
    pen.color("black")
    pen.setheading(90)
    angle = (m / 60) * 360 + (s / 60) * 6
    pen.right(angle)
    pen.pendown()
    pen.forward(180)

    # Draw second hand
    pen.up()
    pen.goto(0, 0)
    pen.color("red")
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.right(angle)
    pen.pendown()
    pen.forward(190)


while True:
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    pen.clear()
    draw_clock(hour, minute, second)

    window.update()

window.mainloop()
