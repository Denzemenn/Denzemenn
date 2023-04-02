from musicbox import MusicBox

player = MusicBox

while True:
    player.play()
    guess = input("Что ты услышал?")
    if guess == "":
        break
    player.check(guess)

    print("Score: ", player.get_score())










