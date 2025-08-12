# Triangle Type Checker
# Question: Write a Python program to check whether a triangle is Equilateral, Isosceles, or Scalene.
# Also, check if the given sides can form a valid triangle.

print("Enter All 3 sides of Triangle\n")

# Step 1: Take inputs for all three sides of the triangle
a = int(input("Enter 'A' side of Triangle: "))
b = int(input("Enter 'B' side of Triangle: "))
c = int(input("Enter 'C' side of Triangle: "))

# Step 2: First, check the triangle validity using the Triangle Inequality Theorem
# The sum of any two sides must be greater than the third side
if a + b > c and b + c > a and a + c > b:

    # Step 3: Check the type of triangle
    if a == b == c:
        # All sides equal → Equilateral triangle
        print("It is an Equilateral triangle !!")
    elif a == b or a == c or b == c:
        # Any two sides equal → Isosceles triangle
        print("It is an Isosceles Triangle !!")
    else:
        # All sides different → Scalene triangle
        print("It is a Scalene Triangle !!")
else:
    # If triangle inequality is not satisfied
    print("It is not a Triangle !! Please Enter Valid Input")
