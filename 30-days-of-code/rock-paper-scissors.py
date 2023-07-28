from getpass import getpass as input

print("Welcome to The 🪨 📄 ✂️ Areena!")
print()
print("Select your move (R, P or S)> ")
player_1 = input("Player 1 >")
player_2 = input("Player 2 >")
if player_1 == "r":
    if player_2 == "r":
        print("Player 1's rock and hitting against Player 2's rock! Its a draw!")
    elif player_2 == "p":
        print("Player 2's paper smothers Player 1's rock! ")
    elif player_2 == "s":
        print("Player 1's rock smashed Player 2's scissors!")
    else:
        print("Invalid move by Player 2.")
elif player_1 == "p":
    if player_2 == "r":
        print("Player 1's paper smothers Player 2's rock! Player 2 is the winner!")
    elif player_2 == "p":
        print("Its a draw! You both chose paper.")
    elif player_2 == "s":
        print("Player 2's scissors shred Player 1's paper into a million pieces!")
    else:
        print("Invalid move by player 2")
elif player_1 == "s":
    if player_2 == "r":
        print("Player 2's rock smashed Player 1's scissors!")
    elif player_2 == "p":
        print("Player 1's scissors shreds Player 2's paper into a million pieces!")
    elif player_2 == "s":
        print("Its a draw! You both chose scissors:")
    else:
        ("Invalid move by Player 2")
else:
    print("Invalid move by Player 1")
