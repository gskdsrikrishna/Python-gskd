#Big Ben Clock Animation:
import turtle
import datetime

window = turtle.Screen()
window.bgcolor("black")
window.title("Big Ben Clock")
window.setup(width=800, height=600)
window.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(4)

def draw_clock():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    pen.up()
    pen.goto(0, -200)
    pen.setheading(90)
    pen.color("white")
    pen.pendown()
    pen.circle(200)

    # Draw hour hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    angle = (hour / 12) * 360 + (minute / 60) * 30
    pen.right(angle)
    pen.pendown()
    pen.forward(100)

    # Draw minute hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    angle = (minute / 60) * 360 + (second / 60) * 6
    pen.right(angle)
    pen.pendown()
    pen.forward(150)

    # Draw second hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("red")
    pen.setheading(90)
    angle = (second / 60) * 360
    pen.right(angle)
    pen.pendown()
    pen.forward(180)

    window.update()

while True:
    draw_clock()
    window.update()

turtle.done()