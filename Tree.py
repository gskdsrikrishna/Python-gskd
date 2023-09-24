#Draw a tree:
import turtle
def draw_tree(branch_len, pen_size):
    if branch_len < 5:
        return
    else:
        turtle.pensize(pen_size)
        turtle.forward(branch_len)
        turtle.right(20)
        draw_tree(branch_len - 15, pen_size - 1)
        turtle.left(40)
        draw_tree(branch_len - 15, pen_size - 1)
        turtle.right(20)
        turtle.backward(branch_len)
turtle.left(90)
turtle.up()
turtle.backward(100)
turtle.down()
turtle.color("green")
draw_tree(75, 7)
turtle.done()