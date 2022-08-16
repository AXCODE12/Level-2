from tkinter import messagebox, simpledialog, Tk,Canvas
import math
k = Tk()
k.withdraw()
# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
an = simpledialog.askinteger('q','Write a radius')
aw = simpledialog.askstring('q', 'Would you like to calculate the area or circumference of a circle?')
if aw == 'area':
    area = math.pi * an * an
    messagebox.showinfo('a',area)
else:
    cir = math.pi * 2 * an
    messagebox.showinfo('a', cir)
#Area = πr^2
#Circumference = 2πr 