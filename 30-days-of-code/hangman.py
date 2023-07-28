import random
words_list = ["abruptly", "bookworm", "cobweb", "dizzy", "equip",
              "funny", "gossip", "haphazard", "lucky", "microwave"]


word = random.choice(words_list)
letter_picked = []
lives = 6
print(word)
print()

while True:
    print()
    letter = input("Choose a letter: ")
    if letter in letter_picked:
        print("You have already picked that letter ")
        print()
        continue
    letter_picked.append(letter)

    all_letters = True
    if letter in word:
        print("You picked the correct letter! ")
        print()
    else:
        print("You picked an incorrect letter! Try again")
    lives -= 1
    for i in word:
        if i in letter_picked:
            print(i, end="")
        else:
            print("_", end="")
            all_letters = False
    print()
    if all_letters:
        print(f"You won the game with {lives} lives left. ")
        break
    if lives <= 0:
        print(f"You lost the game! The correct word was {word}")
