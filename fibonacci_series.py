# Write a Python program to generate a Fibonacci series up to the number of terms entered by the user.

num = int(input("Enter the number of terms: "))

# First two Fibonacci numbers
a = 0
b = 1

# Generate and display the Fibonacci series
for _ in range(num):
    print(a)
    a, b = b, a + b
