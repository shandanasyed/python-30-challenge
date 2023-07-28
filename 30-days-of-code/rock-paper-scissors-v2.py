from getpass import getpass as input

print("Welcome to The 🪨 📄 ✂️ Areena!")
print()

score_1 = 0
score_2 = 0

while True:
    print("Select your move (R, P or S)> ")
    player_1 = input("Player 1 >")
    player_2 = input("Player 2 >")
    if player_1 == "r":
        if player_2 == "r":
            print("Player 1's rock and hitting against Player 2's rock! Its a draw!")
        elif player_2 == "p":
            print("Player 2's paper smothers Player 1's rock! ")
            score_2 += 1
        elif player_2 == "s":
            print("Player 1's rock smashed Player 2's scissors!")
            score_1 += 1
        else:
            print("Invalid move by Player 2.")
    elif player_1 == "p":
        if player_2 == "r":
            print("Player 1's paper smothers Player 2's rock! Player 2 is the winner!")
            score_1 += 1
        elif player_2 == "p":
            print("Its a draw! You both chose paper.")
        elif player_2 == "s":
            print("Player 2's scissors shred Player 1's paper into a million pieces!")
            score_2 += 1
        else:
            print("Invalid move by player 2")
    elif player_1 == "s":
        if player_2 == "r":
            print("Player 2's rock smashed Player 1's scissors!")
            score_2 += 1
        elif player_2 == "p":
            print("Player 1's scissors shreds Player 2's paper into a million pieces!")
        elif player_2 == "s":
            print("Its a draw! You both chose scissors:")
            score_1 += 1
        else:
            ("Invalid move by Player 2")
    else:
        print("Invalid move by Player 1")
        continue
    if score_1 == 3 or score_2 == 3:
        break
print("Gameover!")
if score_1 > score_2:
    print("Player 1 is the winner.")
else:
    print("Player 2 gets the trophy.")
print("Final score:")
print("Player 1: ", score_1)
print("Player 2: ", score_2)
