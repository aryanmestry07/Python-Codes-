# Write a Python program to calculate the factorial of a number entered by the user.

a = int(input("Enter a number: "))

# Initialize factorial result
fact = 1

# Calculate factorial using a for loop
for i in range(1, a + 1):
    fact *= i

# Display the result
print(f"The factorial of {a} is: {fact}")
