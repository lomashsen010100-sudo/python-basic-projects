print("======================= Welcome to guess king game mode ==============================")

import random

n = random.randint(1, 10)

while True:
    user = int(input("Guess a number between 1 to 10 :="))

    if user ==n:
        print("you are won")
        break

    else:
        print("you are lost")