import turtle
from figures import draw_square, draw_triangle, draw_rectangle  # Import the functions from figures.py

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)


pen.penup()
pen.goto(-100, 100)  # Move to the first location
pen.pendown()
draw_square(pen, 100)  

pen.penup()
pen.goto(150, -150)  # Move to the second location
pen.pendown()
draw_square(pen, 100)


pen.penup()
pen.goto(-150, -150)  # Move to the first location
pen.pendown()
draw_triangle(pen, 100)  

pen.penup()
pen.goto(200, 200)  # Move to the second location
pen.pendown()
draw_triangle(pen, 100)


pen.penup()
pen.goto(-240, 220)  # Move to the first location
pen.pendown()
draw_rectangle(pen, 150, 100)  

pen.penup()
pen.goto(260, -200)  # Move to the second location
pen.pendown()
draw_rectangle(pen, 150, 100)

pen.hideturtle()
window.mainloop()
