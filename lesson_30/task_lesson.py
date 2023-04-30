from tkinter import *
from random import *
# =========================================== ЗАДАЧА 1 =================================================

#
# root = Tk()
# root.title("Авторизация")
#
# login_label = Label(root, text="Логин:")
# login_label.grid(row=0, column=0, padx=5, pady=5)
#
# login_entry = Entry(root)
# login_entry.grid(row=0, column=1, padx=5, pady=5)
#
# password_label = Label(root, text="Пароль:")
# password_label.grid(row=1, column=0, padx=5, pady=5)
#
# password_entry = Entry(root, show="*")
# password_entry.grid(row=1, column=1, padx=5, pady=5)
#
# authorize_button = Button(root, text="Авторизация")
# authorize_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
#
# root.mainloop()

# =========================================== ЗАДАЧА 2 =================================================

# root = Tk()
# root.title("Неуловимая кнопка")
# root.geometry("1000x1000")
#
# button = Button(root, text="Нажми меня!")
# button.pack()
#
# def move_button():
#     x = randint(0, 900)
#     y = randint(0, 900)
#     button.place(x=x, y=y)
#
# button.bind("<Enter>", lambda event: move_button())
#
# root.mainloop()

# =========================================== ЗАДАЧА 3(НЕ РАБОТАЕТ) =================================================

# root = Tk()
#
#
#
# rb1 = Radiobutton(root, state='disabled')
# rb2 = Radiobutton(root, state='disabled')
# rb3 = Radiobutton(root, state='disabled')
# rb4 = Radiobutton(root, state='disabled')
# rb5 = Radiobutton(root, state='disabled')
#
# rb1.pack(side="left")
# rb2.pack(side="left")
# rb3.pack(side="left")
# rb4.pack(side="left")
# rb5.pack(side="left")
#
# rb1.deselect()
# rb2.deselect()
# rb3.deselect()
# rb4.deselect()
# rb5.deselect()
#
#
# def select_next():
#     for rb in [rb1, rb2, rb3, rb4, rb5]:
#         if not rb['state'] == 'disabled':
#             rb.deselect()
#             rb.tk_focusNext().select()
#             break
#
#
# root.after(1000, select_next)
#
# root.mainloop()

