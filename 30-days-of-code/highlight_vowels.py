vowels = ["a", "e", "i", "o", "u"]
my_string = input("Enter a sentence: ")
for i in my_string:
    if i.lower() in vowels:
        print("\033[0;31m", end="")
    print(i, end="")
    print("\033[0m", end="")
