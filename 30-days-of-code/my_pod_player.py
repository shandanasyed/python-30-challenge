from replit import audio
import os
import time


def play():
    source = audio.play_file('audio.wav')
    source.paused = False  # unpause the playback
    while True:
        stop_playing = input(
            "Press 2 key to stop playing and go back to main menu: ")
        if stop_playing == "2":
            source.paused = True
            return
        else:
            continue


while True:
    os.system("clear")
    print("🎵 MyPOD Music Player")
    time.sleep(1)
    print("Press 1 to Play")
    time.sleep(1)
    print("Press 2 to Exit")
    print()
    time.sleep(1)
    print("Press anyting else to see the menu again")
    key = input()
    if key == "1":
        play()
    elif key == "2":
        exit()
    else:
        continue
    # take user's input

    # check whether you should call the play() subroutine depending on user's input


play()

# clear the screen

# Show the menu

# take user's input

# check whether you should call the play() subroutine depending on user's input
