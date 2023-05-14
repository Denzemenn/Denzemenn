n = int(input())
d = 0

for i in range(n):
    am = input()
    op = am.split()
    z = int(op[0])
    x = int(op[1])
    c = int(op[2])
    if z + x + c >= 2:
        d += 1
print(d)


