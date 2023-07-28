
import os
import time
print("\033[1;31m", "TODO List Manager", "\033[1;37m")
print()

myList = []


def changeColor(color):
    if color == "red":
        return ("\033[0;31m")
    elif color == "white":
        return ("\033[0;37m")
    elif color == "green":
        return ("\033[0;32m")
    elif color == "lightgreen":
        return ("\033[1;32m")
    elif color == "blue":
        return ("\033[0;34m")
    elif color == "purple":
        return ("\033[0;35m")


def addItem():
    myList.append(item)


def removeItem():
    myList.remove(item)


def printList():
    print(f"{changeColor('purple')}{myList}{changeColor('white')}")


while True:
    command = input(
        f"What do you want to do: {changeColor('green')}add,{changeColor('blue')} view {changeColor('white')}or {changeColor('red')}edit? {changeColor('white')}")
    if command == "view":
        printList()
    elif command == "add":
        item = input(
            f"{changeColor('green')}What item do you want to add?{changeColor('white')}")
        addItem()
        printList()
    elif command == "edit":
        item = input(
            f"{changeColor('red')}Which item do you want to mark as completed and remove?{changeColor('white')}")
        if item in myList:
            removeItem()
            printList()
        else:
            print(f"{item} not in list.")

    elif command == "quit":
        print("Have a good day! 😊")
        break

    time.sleep(2)
    os.system("clear")
