print("Fill in the blank lyrics! (Type in the blank lyrics and see if you areas old 👵🏻(cool) as me! ")
attempts = 1
while True:
    word = input(
        "Every now and then I get a little bit tired Of listening to the sound of my _____. \n")
    if word == "tears":
        break
    else:
        print("Nopes. Try again.")
        attempts += 1

print("Great! It only took you", attempts, "attempt(s).")
