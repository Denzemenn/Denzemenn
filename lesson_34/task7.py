from random import randint
am = 10
mn = set()
while am > 0:
    n = randint(0,15)
    am -= 1
    mn.add(n)
print(list(mn))

