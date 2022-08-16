import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    bye = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    q = simpledialog.askstring('q','What shape do you want to draw: circle, square, triangle?')
    # Draw the shape requested by the user using if-elif-else statements
    if q == 'circle':
        bye.circle(40, steps=50)
    elif q == 'square':
        for i in range(4):
            bye.forward(60)
            bye.left(90)
    else:
        for i in range(3):
            bye.forward(60)
            bye.left(120)
    # Call the turtle .done() method
    turtle.done()