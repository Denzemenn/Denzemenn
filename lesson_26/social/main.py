from user import User

u1 = User("черенков", "денис", "denzemenn", "135797531")
u2 = User()

users = [u1, u2]
l = input("Логин: ")
p = input("Пароль: ")
for u in users:
    if u.log_in(l, p):
        print("ты вошёл в моё оч- тоесть в аккаунт!")
        current_user = u


