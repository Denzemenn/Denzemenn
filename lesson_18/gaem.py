import easygui as ez
import random


def rock_paper_scissors():
    n = "img/n.png"
    k = "img/k.png"
    b = "img/b.png"

    vtm = random.choice([n, b, k])
    x = ez.buttonbox(
        title="Rock, Paper and Scissors.",
        images=[n, b, k],
        msg="Choose one.",
        choices=("close",)
    )
    if x == n and vtm == n: ez.msgbox(msg="Nobody won.")
    elif x == b and vtm == b: ez.msgbox(msg="Nobody won.")
    elif x == k and vtm == k: ez.msgbox(msg="Nobody won.")
    elif x == k and vtm == b: ez.msgbox(msg="You lost.")
    elif x == k and vtm == n: ez.msgbox(msg="You won.")
    elif x == b and vtm == k: ez.msgbox(msg="You won.")
    elif x == b and vtm == n: ez.msgbox(msg="You lost.")
    elif x == n and vtm == k: ez.msgbox(msg="You lost.")
    elif x == n and vtm == b: ez.msgbox(msg="You won.")






def guess_the_number():
    ez.msgbox('Здесь будет игра "Угадай число"')


games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = ez.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()