import random

print("NUMBER GUESSING GAME")
print("🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲")
print()
print("HINT: The number is between one and one-million. Let's get started! ")
print()
count = 1
number = random.randint(1, 1000000)
while True:
    guess_n = int(input("Guess the number: "))
    if guess_n < 0:
        print("Lets just drop it")
        exit()
    elif guess_n < number:
        print("\033[33m", "Too low! Try again.", "\033[0m")
        count += 1
        continue
    elif guess_n > number:
        print("\033[31m", "Too high! Try again.", "\033[0m")
        count += 1
        continue
    elif guess_n == number:
        print("\033[32m", "Correct!", "\033[0m")
        print("You guessed the correct number (",
              number, ") in", count, "attempt(s)")
        break
    else:
        print("I don't recognize this number......")
