from random import choice
import playsound

class MusicBox:
    def __init__(self):
        self.__score = 0
        self.__variants = "hyazhyu"
        self.__sequence = choice(self.__variants)

        print(self.__sequence)

    def play(self):
        for letter in self.__sequence:
            playsound.playsound(f"sounds/{letter}.mp3")

    def __next(self):
        __l = len(self.__sequence) + 1
        self.__sequence = ""
        for _ in range(__l):
            self.__sequence += choice(self.__variants)


    def check(self, predp:str):
        if self.__sequence == predp.lower().strip():
            self.__score += 1
            self.__next()
            playsound.playsound("sounds/correct.wav")
        else:
            self.__score -= 0.5
            playsound.playsound("sounds/incorrect.wav")

    def get_score(self):
        return self.__score




















