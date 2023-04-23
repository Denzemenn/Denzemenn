# from tkinter import *

# Задача 1.-----------------------------------------------------------------------------------------

# root = Tk()
# root["bg"] = "lightblue"
# root.geometry("200x100")
#
# lab = Label(root, text="...")
# lab.pack()
#
# ent = Entry(root, bd=1)
# ent.pack()
#
# def replace(event):
#     lab['text'] = ent.get()
#
# ent.bind("<Button-3>", replace)
#
#
#
# root.mainloop()

# Задача 2.-----------------------------------------------------------------------------------------

#
# root = Tk()
# root.geometry("200x100")
#
# def viewSelected():
#     lab['text'] = "Hello " + radio_choice.get()
#
# lab = Label(root, text="Hello ")
# lab.pack()
#
# radio_choice = StringVar()
#
# rad = Radiobutton(root, text="World", variable=radio_choice, value="World", command=viewSelected)
# rad.pack()
#
# rad2 = Radiobutton(root, text="Python", variable=radio_choice, value="Python", command=viewSelected)
# rad2.pack()
#
# root.mainloop()

# Задача 3.-----------------------------------------------------------------------------------------

# root = Tk()
# root.geometry("200x100")
#
# def switch():
#     if btn['state'] == "disabled":
#         btn['state'] = "normal"
#         btn['text'] = "Активен!"
#     else:
#         btn['state'] = "disabled"
#         btn['text'] = "Не активен!"
#
# val = BooleanVar()
# cb = Checkbutton(root, text="Активировать",
#                  variable=val,
#                  command=switch,
#                  onvalue=True,
#                  offvalue=False)
# cb.select()
# cb.pack()
#
# btn = Button(root, text="Активен", state="normal")
# btn.pack()
#
#
#
#
# root.mainloop()

# Задача 4.-----------------------------------------------------------------------------------------

#
# root = Tk()
# root.geometry("300x200")
#
# lab = Label(root, text="Я текст, а ты?", font="Verdana 20")
# lab.pack()
#
# def bold():
#     if val1.get() == True:
#         lab["font"] += " bold"
#     else:
#         lab["font"] = lab["font"].replace(" bold", "")
# def italic():
#     if val2.get() == True:
#         lab["font"] += " italic"
#     else:
#         lab["font"] = lab["font"].replace(" italic", "")
# def overstrike():
#     if val3.get() == True:
#         lab["font"] += " overstrike"
#     else:
#         lab["font"] = lab["font"].replace(" overstrike", "")
#
# def underline():
#     if val4.get() == True:
#         lab["font"] += " underline"
#     else:
#         lab["font"] = lab["font"].replace(" underline", "")
#
# val1 = BooleanVar()
# cb1 = Checkbutton(root, text="Жирный", variable=val1, onvalue=True, offvalue=False, command=bold)
# cb1.pack()
#
# val2 = BooleanVar()
# cb2 = Checkbutton(root, text="Курсив", variable=val2, onvalue=True, offvalue=False, command=italic)
# cb2.pack()
#
# val3 = BooleanVar()
# cb3 = Checkbutton(root, text="Зачёркнутый", variable=val3, onvalue=True, offvalue=False, command=overstrike)
# cb3.pack()
#
# val4 = BooleanVar()
# cb4 = Checkbutton(root, text="Подчёркнутый", variable=val4, onvalue=True, offvalue=False, command=underline)
# cb4.pack()
#
#
# root.mainloop()

# Задача 5.-----------------------------------------------------------------------------------------

# root = Tk()
# root.geometry("500x300")
# root["bg"] = "white"
#
# x = ["#FAFAEB", "#7676EE", "#8B8B23", "#EEEEC5", "#8B8B73", "#0000FF"]
#
# def colorchange(event):
#     scala_val = scala.get()
#     if scala_val == 0:
#         root["bg"] = x[0]
#     elif scala_val == 1:
#         root["bg"] = x[1]
#     elif scala_val == 2:
#         root["bg"] = x[2]
#     elif scala_val == 3:
#         root["bg"] = x[3]
#     elif scala_val == 4:
#         root["bg"] = x[4]
#     else:
#         root["bg"] = x[5]
#
# scala = Scale(root, from_=0, to_=5, orient="horizontal", length=300, command=colorchange)
# scala.pack()
#
#
# root.mainloop()

# Задача 6.-----------------------------------------------------------------------------------------

# root = Tk()
# root.geometry("600x650")
#
# def uvazheniye(event):
#     ent.get()
#     ent.insert(END, ", пожалуйста 🙏")
#
# img = PhotoImage(file='уваж.png').subsample(2, 2)
# Label(root, image=img).pack()
#
# ent = Entry(root, width=50)
# ent.pack()
#
# btn = Button(root, text="Добавить уважения", width=25)
# btn.pack()
#
# btn.bind("<Button-1>", uvazheniye)
#
# root.mainloop()

# Конец 😳
