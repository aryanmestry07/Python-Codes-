# Program to check if a given string is a palindrome

# Take input string from user
s = input("Enter a string: ")

# Initialize an empty string to store the reversed version
rev = ""

# Reverse the string by prepending each character
for char in s:
    rev = char + rev

# Compare original string with the reversed string
if s == rev:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

print()  # Print a blank line for cleaner output
