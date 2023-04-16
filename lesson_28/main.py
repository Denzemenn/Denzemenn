from tkinter import *
#
# def hell_o(event):
#     #print("ocherednoy hellou vorld")
#     message=ent.get()
#     ent.delete(0, END)
#     print(message)
#
#     message2 = txt.get(1.0, END)
#     txt.delete(0.0, END)
#     print(message2)
#
# root = Tk()
# root.title("uhm.. i dont even know what to type in there")
# root.geometry("800x1000")
# root['bg'] = "wheat"
#
# lab = Label(root, text="Xristos voskres!\n"
#                        "Voistinu voskres!" )
# lab["bg"] = "#ab54cd"
# lab["fg"] = "silver"
# lab["font"] = ("times new roman", 40, "italic", "bold")
# lab.pack()
#
# btn = Button(root,
#              text="alyo zachem zhmyosh",
#              font=("times new roman", 40, "italic", "bold"),
#              width=30,
#              height=1,
#              bd=5,
#              #command=hell_o
#              )
#
# btn.pack()
# btn.bind("<Button-1>", hell_o)
# #Button-1 - ЛКМ
# #Button-3 - ПКМ
# #Double-Button-1 - 2 ЛКМ
#
# ent = Entry(root, bd=5, width=30,font=("times new roman", 20, "italic", "bold"))
# ent.pack()
#
# txt = Text(root, width=20, height=5)
# txt.pack()

# root = Tk()
# root.title(" ")
# root.geometry("150x300"
#               "")
# root['bg'] = "#B0B0E0"
#
# lab = Label(root, text="голубой", width=6)
# lab["bg"] = "#EEEECB"
# lab["fg"] = "black"
# lab["font"] = ("times new roman", 20, "italic", "bold")
# lab.pack()
#
# ent = Entry(root, font=("times new roman", 20, "italic", "bold"), width=7)
# ent.pack()
#
# btn1 = Button(root,width=13, height=1)
# btn1["bg"] = "red"
# btn1.pack()
#
# btn2 = Button(root,width=13, height=1)
# btn2["bg"] = "orange"
# btn2.pack()
#
# btn3 = Button(root,width=13, height=1)
# btn3["bg"] = "yellow"
# btn3.pack()
#
# btn4 = Button(root,width=13, height=1)
# btn4["bg"] = "green"
# btn4.pack()
#
# btn5 = Button(root,width=13, height=1)
# btn5["bg"] = "lightblue"
# btn5.pack()
#
# btn6 = Button(root,width=13, height=1)
# btn6["bg"] = "purple"
# btn6.pack()
#
# btn7 = Button(root,width=13, height=1)
# btn7["bg"] = "red"
# btn7.pack()
# root.mainloop()

# def send(event):
#     message1 = ent1.get()
#     ent1.delete(0, END)
#     print(message1)
#
#     message2 = txt.get(1.0, END)
#     txt.delete(0.0, END)
#     print(message2)
#
#
#
#
#
# root = Tk()
# root.title("Отправка комментария")
# root.geometry("250x350")
#
# lab1 = Label(root, text="Ваш адрес:", bg="peachpuff2")
# lab1.pack()
#
# ent1 = Entry(root, bd=3)
# ent1.pack()
#
# lab2 = Label(root, text="Комментарий:", bg="peachpuff2")
# lab2.pack()
#
# txt=Text(root, bd=1, width=20, height=5)
# txt.pack()
#
# btn = Button(root, text="Отправить", bg="lightblue", bd=2)
# btn.pack()
# btn.bind("<Button-1>", send)
#
#
#
# root.mainloop()

# root = Tk()
# root.geometry("40x80")
#
#
# lab = Label(root, text="Хелоу")
# lab["font"] = "Verdana 20"
# lab.pack()
# def normal(event):
#     lab["font"] = lab["font"].replace("italic", "").replace("bold", "")
# def italic(event):
#     lab["font"] = lab["font"].replace("italic", "")
#     lab["font"] = lab["font"] + " italic"
# def bold(event):
#     lab["font"] = lab["font"].replace("bold", "")
#     lab["font"] = lab["font"] + " bold"
#
# lab.bind("<Button-1>", normal)
# lab.bind("<Button-3>", italic)
# lab.bind("<Double-Button-1>", bold)
#
# root.mainloop()


root = Tk()
root.geometry("200x200")

lab = Label(root, text="text")
lab.pack()

ent = Entry(root)
ent.pack()

btn = Button(root)
btn.pack()

def set_text(event):
    enter = ent.get()
    ent.delete(0, END)
    lab["text"] = enter

btn.bind("<Button-1>", set_text)
root.mainloop()

















































































































root.mainloop()







































