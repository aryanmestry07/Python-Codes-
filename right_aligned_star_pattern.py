# Write a Python program to display the following pattern based on the number of rows entered by the user:
# Example for rows = 5:
#     *
#    **
#   ***
#  ****
# *****

# Input: number of rows
rows = int(input("Enter the number of rows: "))

# Loop to print the right-aligned pattern
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)
