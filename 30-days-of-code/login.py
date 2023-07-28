print("System Login:")
print()


def login():
    while True():
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username != "espresso" and password != "erikoiskahvi":
            print("Wrong username or password. Please try again")
            continue
        else:
            print("Welcome aboard. Have a nice time!")
            break


login()
