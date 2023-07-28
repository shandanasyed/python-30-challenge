print("Infinity Dice 🎲")
print()
sides = int(input("How many sides?: "))
leave_game = "yes"


def roll_dice(s):
    import random
    print("You rolled", random.randint(0, s))


while leave_game == "yes":
    roll_dice(sides)
    print()
    leave_game = input("Roll again? ")
    print()
