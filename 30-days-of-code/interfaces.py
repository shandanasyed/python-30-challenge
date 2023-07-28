
def color(color):
    if color == "red":
        return ("\033[0;31m")
    elif color == "green":
        return ("\033[0;32m")
    elif color == "purple":
        return ("\033[0;35m")
    elif color == "white":
        return ("\033[1;37m")
    elif color == "blue":
        return ("\033[0;34m")
    elif color == "yellow":
        return ("\033[1;33m")


# Interface 1:
title = f"{color('red')}={color('white')}={color('blue')}= Music App {color('blue')}={color('white')}={color('red')}="


song = "Queen"
prev = "PREV"
next = "NEXT"
pause = "PAUSE"

print()
print(f"             {title:^35}")
print()
print(f"🔥▶️     {color('white')}Radio Gaga")
print(f"{color('yellow')}{song:>13}")
print()
print(f"{color('white')}{prev}")

print(f"{color('green')}{next:>9}")

print(f"{color('purple')}{pause:>15}")

print()
print("________________________________")
print()
print()
# Interface 2
line_1 = "WELCOME TO"
line_2 = "--   ARMBOOK   --"
main = "Definitely not a rip off of"
main2 = "a certain other social"
main3 = "networking site."
line_3 = "honest"
username = "Username:"
password = "Password:"

print(f"    {color('white')}{line_1:^35}")
print(f"    {color('blue')}{line_2:^35}")
print()
print(f"{color('yellow')}{main: >35}")
print(f"{main2: >35}")
print(f"{main3: >35}")
print()
print(f"{color('red')}{line_3:^45}")
print()
print(f"{color('white')}{username:^45}")
print(f"{password:^45}")
