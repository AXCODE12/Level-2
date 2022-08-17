from tkinter import messagebox, simpledialog, Tk
Hi = Tk()
Hi.withdraw()

"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
que1 = simpledialog.askinteger('q','Write a number')
que2 = simpledialog.askinteger('q','Write another number')
messagebox.showinfo('ans', que1 + que2)