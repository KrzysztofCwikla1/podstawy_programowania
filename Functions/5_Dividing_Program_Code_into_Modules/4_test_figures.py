# draw_figures.py
import turtle
from figures import draw_square  

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create a turtle instance
pen = turtle.Turtle()

# Side length
side_length = 100


draw_square(pen, side_length)


# Keep the window open until it is clicked to close
window.mainloop()
