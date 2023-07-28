
first, last, mother, city = input(
    "Enter your \n first name \n last name \n mother's maiden name \n city of birth \n all separated by spaces: ").split(" ")

first_name = first[0:3].title()
last_name = last[0:3].lower()
maiden_name = mother[:2].title()
birth_city = city[-3:].lower()

print(
    f"Your Star Wars name is {first_name+last_name} {maiden_name+birth_city}")
