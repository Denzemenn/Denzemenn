import random

life = 10
length = 3

answer = random.randint(100, 999)
answer = str(answer)

while life:
    is_guessed = False
    print("=" * 10)

    print("Lives:", life)

    guess = input("Guess: ")
    if len(guess) != length or not guess.isdigit():
        print("Only numbers between 100 and 999")
        continue
    if guess == answer:
        print("yay u won")
        is_guessed = True
        break

    if not is_guessed:
        for i in range(length):
            if guess[i] == answer[i]:
                print("fermi")
                is_guessed = True
                break

    if not is_guessed:
        for char in guess:
            if char in answer:
                print("pico")
                is_guessed = True
                break
    if not is_guessed:
        print("bagels")

    life -= 1
































