print("30 Days Down")
print()
for i in range(1, 30):
    print(f"Day {i}:")
    opinion = input()
    text = f"You thought Day {i} was"
    print(f"{text:^35}")
    print(f"{opinion:^35}")
    print()
