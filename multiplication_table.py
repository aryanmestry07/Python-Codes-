# multiplication_table.py
# ----------------------------------------
# Question:
# Write a Python program to print the multiplication table 
# for any number entered by the user.

print("Multiplication Table Generator:\n")

num = int(input("Enter a number: "))

# Loop from 1 to 10 to generate the multiplication table
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
