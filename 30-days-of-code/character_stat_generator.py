def roll_dice(number):
    import random
    return random.randint(1, number)


def health():
    return roll_dice(6) * roll_dice(8)


print("⚔️ Character Stats Generator 💀")
print()

go_on = "yes"
while go_on == "yes":
    character = input("Name you warrior: ")
    print("Their health is: ", health(), "hp")
    go_on = input("More? yes or no? ")
