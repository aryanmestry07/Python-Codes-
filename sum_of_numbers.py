# Question:
# Write a Python program to calculate the sum of all numbers 
# between 1 and a number entered by the user (inclusive).

print("Sum Calculator:\n")

a = int(input("Enter a number: "))
total_sum = 0

# Calculate sum of numbers from 1 to a
for i in range(1, a + 1):
    total_sum += i

print(f"The sum of numbers from 1 to {a} is: {total_sum}")
