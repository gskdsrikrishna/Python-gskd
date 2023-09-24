import turtle

def draw_smiley_face():
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.circle(100)  # Draw face
    turtle.penup()
    turtle.goto(-40, 40)
    turtle.pendown()
    turtle.circle(10)   # Draw left eye
    turtle.penup()
    turtle.goto(40, 40)
    turtle.pendown()
    turtle.circle(10)   # Draw right eye
    turtle.penup()
    turtle.goto(-40, 0)
    turtle.pendown()
    turtle.setheading(-60)
    turtle.circle(40, 120)  # Draw smile

draw_smiley_face()
turtle.done()