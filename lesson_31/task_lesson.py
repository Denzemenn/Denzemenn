from tkinter import *


x = 0
root = Tk()
root.geometry("550x550")

# ==================================  ZADACHA 1 =========================================

# c = Canvas(root, width=500, height=500, bg="silver")
# c.pack(anchor=CENTER, expand=True)
#
# c.create_text(int(c["width"]) / 2, 250, text=x, font="verdana 25")
# img = PhotoImage(file="еда.png").subsample(5, 5)
# c.create_image(250, 250, image=img)
#
# def schitalka():
#     global x
#     x = x + 1
#     c.after(1000, schitalka)
#     c.delete("all")     # очисточка
#     c.create_text(250, 250, text=x, font="verdana 25")
#     c.create_image(250, 250, image=img)
#     if x == 15:
#         root.destroy()
# c.after(1000, schitalka)
#

# ==================================  ZADACHA 3 =========================================

c = Canvas(root, width=500, height=500, bg="silver")
c.pack(anchor=CENTER, expand=True)



l = None
p = None

def pos1(pelmeni):
    global l
    l = (pelmeni.x, pelmeni.y)

def pos2(inemlep):
    global p
    p = (inemlep.x, inemlep.y)

def build():
    c.create_line(l[0], l[1],
                  p[0], p[1])

b = Button(root, text="build", command=build)
b.pack()

c.bind("<Button-1>", pos1)
c.bind("<Button-3>", pos2)



















root.mainloop()