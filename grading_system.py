# Write a program that asks the user to input a score (0-100)
# Based on the score, print the corresponding grade:
# A: 90 to 100
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
# F: Below 60

score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Your grade is A !!")
elif 80 <= score <= 89:
    print("Your grade is B !!")
elif 70 <= score <= 79:
    print("Your grade is C !!")
elif 60 <= score <= 69:
    print("Your grade is D !!")
else:
    print("You are fail")
