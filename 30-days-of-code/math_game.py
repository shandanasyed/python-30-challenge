print("MATH GAME! ✖️")
print()
multiples_of = int(input("Name your multiples: "))
score = 0
for i in range(1, 11):
    print(i, "x", multiples_of, "=")
    answer = int(input("> "))
    if answer == (i * multiples_of):
        print("Great work!")
        score += 1
    else:
        print("Nopes. The answer was ", i * multiples_of)
        i += 1
print()
print("---")
print()
print("You scored ", score, "out of 10")
