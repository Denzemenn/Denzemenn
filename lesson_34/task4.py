from random import choice

n = int(input())
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
strok = ""
for i in range(n):
    strok += choice(alpha)
print(strok)










