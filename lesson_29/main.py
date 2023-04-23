from tkinter import *

root = Tk()

def scale(val):
    print(s.get())

s = Scale(root, from_=80, to_=99, orient="horizontal", length=300, tickinterval=3, resolution=3, command=scale)
s.pack()




root.mainloop()











