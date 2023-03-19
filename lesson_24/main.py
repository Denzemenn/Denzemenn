# class Mashina:
#     def __init__(self, w:int, d:int, pdk:bool, pr:int):
#         self.wheels = w
#         self.doors = d
#         self.pdk = pdk
#         self.probeg = 10_000
#
#     def go_out(self):
#         if self.pdk == True:
#             self.pdk = False
#             return "Дядя Коля изгнан"
#         else:
#             return "Машина чиста. Его здесь не было."
#
#     def obn(self):
#         self.probeg = 0
#
#     def sell(self):
#         self.obn()
#
# toyota = Mashina(w=8, d=8, pdk=True)
# print(toyota.go_out())
# toyota.pdk = True
# toyota.probeg = 500
# print(toyota.probeg)
# import string
#
# class Alphabet:
#     def __init__(self, lang:str, letters:str):
#         self.lang = "eng"
#         self.letters = string.ascii_lowercase
#     def print(self):
#         return self.letters
#     def nums_am(self):
#         return len(self.letters)
#
#
# alpha = Alphabet()
# print(alpha.print())
# print(alpha.nums_am())

# class Car:
#     def __init__(self, color, type, year):
#         self.color = color
#         self.type = type
#         self.year = year
#     def start_eng(self):
#         return "Автомобиль запущен."
#     def stop_eng(self):
#         return "Автомобиль заглушен."
#     def y_add(self):
#         self.year = 1980
#     def c_add(self):
#         self.color = "baklazhan"
#     def t_add(self):
#         self.type = "lada sedan"
#     def print(self):
#         return self.type, self.color, self.year
# car = Car(type="lada sedan", color="baklazhan", year=1980)
#
# print(car.print())
import datetime

class Clock:
    def __init__(self):
        self.__h, self.__m, self.__s = ["08, 02, 03"]
        # self.__h, self.__m, self.__s = datetime.datetime.now().strftime("%H:%M:%S").split(":")
        self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)
    def addH(self):
        self.__h +=1

    def addM(self):
        self.__m +=1

    def addS(self):
        self.__s +=1

    def vivod(self):
        return f"{self.__h}:{self.__m}:{self.__s.rjust(2, '0')}"
anny = Clock()
anny.addH()
print(anny.vivod())












