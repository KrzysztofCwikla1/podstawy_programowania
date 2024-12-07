# figures.py

def draw_square(t, size):
    """Draw a square with the given turtle t and side length size."""
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_triangle(t, size):
    """Draw a triangle with the given turtle t and side length size."""
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_rectangle(t, width, height):
    """Draw a rectangle with the given turtle t, width, and height."""
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
