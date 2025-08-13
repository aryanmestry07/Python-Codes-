# even_numbers_printer.py
# ----------------------------------------
# Question:
# Write a Python program to print all the even numbers 
# between 1 and a number entered by the user.

print("Even Numbers Finder:\n")

num = int(input("Enter a number: "))

# Loop through even numbers from 2 up to the entered number (inclusive)
for i in range(2, num + 1, 2):
    print(i)
