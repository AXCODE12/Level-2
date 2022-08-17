from tkinter import messagebox, simpledialog, Tk
Hi = Tk()
Hi.withdraw()
"""

* Write a python program that asks the user a minimum of 3 riddles.
    
* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
rid1 = simpledialog.askstring('q','What has a head and tail but no body?')
rid2 = simpledialog.askstring('q','What has rings but no fingers?')
rid3 = simpledialog.askstring('q','What can run but can''t walk?')
score = 0
if rid1 == 'coin':
    score += 1
else:
    messagebox.showinfo('W','Wrong')
if rid2 == 'telephone':
    score += 1
else:
    messagebox.showinfo('W','Wrong')
if rid3 == 'river':
    score += 1
else:
    messagebox.showinfo('W','Wrong')

messagebox.showinfo('score',score)
