from tkinter import *

root = Tk()
root.geometry("600x600")


c = Canvas(root, width=500, height=500, bg="wheat")
c.pack(anchor="center", expand=True)

# ==================================  TEXT =========================================

# c.create_text(250, 250,
#               text="живи. ты ещё нужен людям.",
#               font="verdana 12")

# ==================================  RECTANGLE =========================================

# c.create_rectangle(10, 10,
#                    100, 100,
#                    width=5,
#                    fill="blue",
#                    outline="red")

# ==================================  POLYGON =========================================

# c.create_polygon(10,10,
#                  150,150,
#                  10,150)

# ==================================  OVAL =========================================

# c.create_oval(10, 10,
#               150, 150)

# ==================================  ARC =========================================

# c.create_arc(10, 10, 250, 150, extent=30, start=45)
#
# c.create_arc(10, 10,
#              250, 150,
#              extent=90,
#              start=45,
#              style=CHORD)
#
# c.create_arc(10, 10,
#              250, 150,
#              extent=90,
#              start=45,
#              style=ARC,
#              outline="magenta",
#              width=8)

# ==================================  LINE =========================================

# c.create_line(10, 10,
#               150, 50,
#               arrow="both",
#               width=15,
#               arrowshape=(50, 50, 50))

# ================================== OTRISOVKA =========================================

# c.create_rectangle(10, 10,
#                    100, 100,
#                    width=5,
#                    fill="blue",
#                    outline="red",
#                    activefill="magenta",
#                    activewidth=10)

# ==================================  event =========================================

# def pipipupu(event):
#     print(event)
#
# btn = Button(root, text="booton")
# btn.pack()
# btn.bind("<Button-3>", pipipupu)



root.mainloop()
