import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Pie Chart")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

# Define the data for the pie chart
data = [30, 20, 40, 50, 10]
radius = 200

# Create the turtle for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.goto(0, -radius)

# Function to draw a sector of the pie chart
def draw_sector(angle):
    pen.pendown()
    pen.circle(radius, angle)
    pen.left(90)
    pen.forward(radius)
    pen.left(90)
    pen.penup()
    pen.goto(0, -radius)

# Calculate the total sum of data
total = sum(data)

# Draw the sectors
for d in data:
    angle = 360 * d / total
    draw_sector(angle)

wn.mainloop()
