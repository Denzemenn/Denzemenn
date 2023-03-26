# class Human:
#     def __init__(self, hei=1, fat=100):
#         location = "Новосибирск"
#         __priv = "Что - то"
#
#
#     def public(self):
#         pass
#
#     def __private(self):
#         pass
#
#
# person = Human()


import random

class Human:
    default_name = "Александр"
    default_age = "35"

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def public(self):
        return self.name, self.age

    def __private(self):
        return self.__house, self.__money

    def earn_money(self):
        self.__money += 50

    def default_info(self):
        return Human.default_name, Human.default_age

    def info(self):
        return self.name, self.age, self.__money, self.__house

    def __make_deal(self, dom):
        if self.__money >= dom.final_price():
            self.__money -=  dom.final_price()
            return True

    def buy_house(self, dom):
        if self.__make_deal(dom):
            dom.owner = self.name
            self.__house = dom
            return "Сделка совершена. Дом куплен"
        else:
            return f"Не хватает денег. Нужно {dom.final_price() - self.__money}"






class House:
    def __init__(self, ar, pr):
        self.__area = ar
        self.__price = pr
        self.skidka = random.randint(5, 25) / 100

    def final_price(self):
        return self.__price - (self.__price * self.skidka)

artem = Human()
house1 = House("Новосибирск", 500)
print(house1.final_price())
print(artem.buy_house())

















