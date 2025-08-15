# Write a Python program to display the following pattern based on the number of rows entered by the user:
# Example for num = 5:
# *
# **
# ***
# ****
# *****

# Input: number of rows
num = int(input("Enter the number of rows: "))

# Loop to print the pattern
for i in range(1, num + 1):
    print("*" * i)
