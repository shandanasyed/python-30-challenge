print("Loan Calculator")
print()
print("$1000 over 10 years at an APR of 5%.")
print()
value = 1000


for year in range(10):
    value += value * 0.05
    print("Year", year+1, "is", round(value, 2))

interest = value - 1000
print("You paid $", round(interest, 2), "in interest")
