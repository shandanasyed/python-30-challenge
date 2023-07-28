
while exit != "yes":
    animal = input("What animal do you want? ").lower()
    if animal == "cow":
        print("A cow says mow.🐮")
    elif animal == "cat":
        print("Cat meows.🐈")
    elif animal == "dog":
        print("Dog goes woof woof🐶")
    elif animal == "duck":
        print("Duck says quack quack🐥")
    elif animal == "horse":
        print("Horse goes hee-haa-haa🐴")
    elif animal == "bird":
        print("Bird goes tweet tweet.🐤")
    else:
        print("Sorry I don't know this one. Try another. ")
    exit = input("Do you want to exit? ")
