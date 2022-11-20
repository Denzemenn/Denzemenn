import random as r
import datetime as d

while True:
    number = input("how many birthdays do u wanna generate ")
    if not number.isdigit() or int(number) > 65 or int(number) < 2:
        print("Is this funny for you? Please, enter normally.")
    else:
        number = int(number)
        break


birthdays = []
startOfYear = d.date(2022, 1, 1)
for _ in range(number):
    randomNumberOfDays = d.timedelta(r.randint(0,364))
    birthday = startOfYear + randomNumberOfDays
    birthdays.append(birthday)

for i in range(number):
    print(f"{i + 1}){birthdays[i]}")

print("=" * 10)
for i in set(birthdays):
    if birthdays.count(i) > 1:
        print(f"- {i.strftime('%d.%m.%y')} is here {birthdays.count(i)} times.")




