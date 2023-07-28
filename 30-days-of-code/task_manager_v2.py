import os
import time
print("        📝 TODO List Manager 📔")

toDoList = []


def addItem():
    toDoList.append(item)


def removeItem():
    toDoList.remove(item)


def editItem():
    for i in range(0, len(toDoList)):
        if item == i:
            toDoList[i] = new


def printList():
    print(toDoList)


while True:
    command = input(
        "Do you want to view, add, remove or edit an item? (Press q to quit)")
    if command == "add":
        item = input("What item do you want to add?")

        addItem()
        printList()
    elif command == "remove":
        item = input("What item do you want to remove? (Press q to quit)")
        if item in toDoList:
            check = input(
                f"Are you sure you want to remove {item} from the list?")
            if check == "yes":
                removeItem()
                printList()
            else:
                printList()

        else:
            print("Item not in the list.")
            continue
    elif command == "view":
        printList()
    elif command == "edit":
        item = input("What item do you want to edit? (Press q to quit)")
        new = input("What do you want to change in it?")
        editItem()
        printList()
    elif command == "q":
        exit()
    elif command == "delete":
        toDoList = []
    time.sleep(1)
    os.system("clear")
