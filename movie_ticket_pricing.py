'''
"Movie Ticket Pricing"

Write a Python program that asks the user for their age and whether it is a weekend (yes or no).
Ticket prices are:

Children (age < 13): ₹150 on weekdays, ₹200 on weekends

Teenagers (13 ≤ age ≤ 19): ₹200 on weekdays, ₹250 on weekends

Adults (20 ≤ age ≤ 59): ₹300 on weekdays, ₹350 on weekends

Seniors (age ≥ 60): ₹180 on weekdays, ₹200 on weekends
'''
print("Movie Ticket Pricing \n")
age = int(input("Enter your age : "))
week = input("Is it a Weekend(yes or no) : ").lower()

#Children
if age < 13:
    if week == 'yes':
        print("Ticket Price : ₹200")
    elif week == 'no':
        print("Ticket Price : ₹150")
    else:
        print("Invalid weekend input !!")
#Teenagers
elif  13 <= age <=19:
    if week == 'yes':
        print("Ticket Price : ₹250")
    elif week == 'no':
        print("Ticket Price : ₹200")
    else:
        print("Invalid weekend input !!")
#Adults
elif 20 <= age <= 59:
    if week == 'yes':
        print("Ticket Price : ₹350")
    elif week == 'no':
        print("Ticket Price : ₹300")
    else:
        print("Invalid weekend input !!")
#Seniors
elif age >= 60:
    if week == 'yes':
        print("Ticket Price : ₹200")
    elif week == 'no':
        print("Ticket Price : ₹180")
    else:
        print("Invalid weekend input !!")
else:
    print("Please enter valid age !!")
    
