# x = ["Никита", "Екатерина", "Андрей", "Андрей", "Анастасия", "Арсалан",
#      "Наталья", "Тимур", "Григорий", "Евгений", "Анастасия",  "Екатерина",
#      "Андрей", "Евгения", "Анастасия", "Герман", "Тимур", "Григорий",
#      "Арсалан", "Ярослава", "Есения", "Даниил", "Данил", "Андрей", "Никита"]
#
# n = input().capitalize()
# koljichestvo = 0
#
#
# for eachname in x:
#     if eachname == n:
#         koljichestvo += 1
#
# print(koljichestvo)

# метод 2:

x = ["Никита", "Екатерина", "Андрей", "Андрей", "Анастасия", "Арсалан",
     "Наталья", "Тимур", "Григорий", "Евгений", "Анастасия",  "Екатерина",
     "Андрей", "Евгения", "Анастасия", "Герман", "Тимур", "Григорий",
     "Арсалан", "Ярослава", "Есения", "Даниил", "Данил", "Андрей", "Никита"]

n = input().capitalize()
koljichestvo = x.count(n)
print(koljichestvo)






