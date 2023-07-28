def color_changer(word, color):
    if color == "red":
        print("\033[0;31m", word, sep="", end="")
    elif color == "purple":
        print("\033[0;35m", word, sep="", end="")
    elif color == "cyan":
        print("\033[0;36m", word, sep="", end="")
    elif color == "yellow":
        print("\033[0;34m", word, sep="", end="")
    else:
        print("\033[1;37m", word, sep="", end="")


print("Super subroutine")
print()
print("With my ", end="")
color_changer("new program ", "purple")
color_changer("I can just call red(\"and\") ", "yellow")
color_changer("and ", "red")
color_changer("that word will appear in the color I set it to. \n", "yellow")
print()
color_changer("With no ", "reset")
color_changer("weird gaps.", "cyan")
print()
color_changer("Epic!", "reset")
