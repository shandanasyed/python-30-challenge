print("Exam Grade Calculator")
print("______________________")
print()
exam = input("Enter exam name: ")
max_score = int(input("What is the maximum score in the exam? "))
score = int(input("What is your score? "))
percentage = round(score*100/max_score, 2)
print("You got,", percentage, "%")
if percentage <= 100 and percentage >= 90:
    print("Grade A+")
    print("Excellent! Your worked really hard! 👏🏻")
elif percentage < 90 and percentage >= 80:
    print("Grade A")
    print("Good job! Thats a good score! 👍🏼")
elif percentage < 80 and percentage >= 70:
    print("Grade B")
    print("Not Bad. Perhaps aim higher next time? 🤔 ")
elif percentage < 70 and percentage >= 60:
    print("Grade C")
    print("You need to work harder, better luck next time 🍀 ")
elif percentage < 60 and percentage >= 50:
    print("Grade D")
    print("You definitely need to work harder! 😐")
elif percentage < 50:
    print("Grade U")
    print("Are you for real? 😧 ")
else:
    print("please enter a valid number.")
