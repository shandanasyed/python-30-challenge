my_string = input("Enter a sentence: ")
for i in my_string:
    if i.lower() == "r":
        print("\033[0;31m", end="")
    elif i.lower() == "b":
        print("\033[0;34m", end="")
    elif i.lower() == "p":
        print("\033[0;35m", end="")
    elif i.lower() == "y":
        print("\33[0;33m", end="")
    elif i.lower() == "g":
        print("\33[0;32m", end="")
    elif i == " ":
        print("\033[0m", end="")

    print(i, end="")
