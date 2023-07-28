import random
import time
import os


def char_generator():
    print("Character Builder")
    print()
    time.sleep(1)
    name = input("Name Your Legend: \n")
    print()
    type = input("Character Type (Human, Elf, Wizard, Orc): \n")
    print()
    print(name)


def number_generator(side):
    return random.randint(1, side)


def health_generator():
    return ((number_generator(6)) * (number_generator(12)/2)) + 10


def strength_generator():
    return ((number_generator(6)) * (number_generator(12))/2) + 12


new_character = "y"
while new_character == "y":
    char_generator()
    time.sleep(1)
    print("HEALTH:", health_generator())
    time.sleep(1)
    print("STRENGTH:", strength_generator())
    print()
    time.sleep(1)
    print("May your name go down in Legend......")
    print()
    time.sleep(1)
    new_character = input("Generate another character?: y or n ")
    os.system("clear")
