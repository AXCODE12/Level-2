from tkinter import messagebox, simpledialog, Tk
Hi = Tk()
Hi.withdraw()

"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

que1 = simpledialog.askinteger('q','Write a number')
que2 = simpledialog.askinteger('q','Write another number')
que3 = simpledialog.askstring('q','Would you like to add, subtract, multiply or divide?')

if que3 == 'add':
    messagebox.showinfo('ans', que1 + que2)
elif que3 == 'subtract':
    messagebox.showinfo('ans', que1 - que2)
elif que3 == 'multiply':
    messagebox.showinfo('ans', que1 * que2)
elif que3 == 'divide':
    messagebox.showinfo('ans', que1/que2)
else:
    messagebox.showinfo('ans', 'You did not select one of the operations')