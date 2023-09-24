import turtle

def draw_rotating_star():
    turtle.speed(3)

    for _ in range(36):
        for _ in range(5):
            turtle.forward(100)
            turtle.right(144)
        turtle.right(10)

draw_rotating_star()
turtle.done()
