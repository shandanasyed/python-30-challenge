import random
import time
import os


def char_generator():
    name = input("Name Your Legend: \n")
    print()
    type = input("Character Type (Human, Elf, Wizard, Orc): \n")
    print()
    print(name)


def roll_dice(side):
    return random.randint(1, side)


def health_generator():
    health = ((roll_dice(6)) * (roll_dice(12)/2)) + 10
    return health


def strength_generator():
    strength = ((roll_dice(6)) * (roll_dice(12))/2) + 12
    return strength


play_again = "yes"
while play_again == "yes":
    print("⚔️ BATTLE TIME ⚔️")
    print()

    char_1 = input("Name Your Legend: \n")
    print()
    type_1 = input("Character Type (Human, Elf, Wizard, Orc): \n")
    print(char_1)
    print()
    health_1 = health_generator()
    strength_1 = strength_generator()
    print("HEALTH:", health_1)

    print("STRENGTH:", strength_1)
    print()

    print("Who are they battling? ")
    print()
    time.sleep(1)
    char_2 = input("Name Your Legend: \n")
    print()
    type_2 = input("Character Type (Human, Elf, Wizard, Orc): \n")
    print(char_2)
    print()
    health_2 = health_generator()
    strength_2 = strength_generator()
    print("HEALTH:", health_2)

    print("STRENGTH:", strength_2)
    print()

    round = 1
    winner = None
    play_again = "yes"

    while True:
        time.sleep(1)
        os.system("clear")
        print("⚔️ BATTLE TIME ⚔️")
        print()
        time.sleep(1)
        print("The battle begins!")
        score_1 = roll_dice(6)
        score_2 = roll_dice(6)
        damage = abs(strength_1 - strength_2) + 1
        if score_1 > score_2:
            health_2 -= damage
            print(char_1, "wins round", round, ".", char_2,
                  "takes a hit, with", damage, "damage")
        elif score_1 < score_2:
            health_1 -= damage
            print(char_2, "wins round", round, ".", char_1,
                  "takes a hit, with", damage, "damage")
        else:
            print("It's a draw!", round)

        print()
        print()
        print(char_1)
        print("HEALTH:", health_1)
        print()
        print(char_2)
        print("HEALTH:", health_2)
        print()
        time.sleep(2)

        if health_1 <= 0:
            print(char_1, "has died!💀")
            winner = char_2
            break
        elif health_2 <= 0:
            print(char_2, "has died!💀")
            winner = char_1
            break
        else:
            print("And they are both standing for the next round")
            round += 1

    time.sleep(1)
    os.system("clear")
    print("⚔️ BATTLE TIME ⚔️")
    print()
    print(winner, "has won in", round, "rounds")
    play_again = input("Play again? yes or no?")
    if play_again == "yes":
        continue
    else:
        break
