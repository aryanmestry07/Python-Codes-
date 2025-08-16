# Menu-driven program for various operations
# Armstrong, Reversed, Factorial, Fibonacci, and Palindrome

while True:
    print("\nMenu")
    print("Enter 'Armstrong' for Armstrong")
    print("Enter 'Reversed' for Reversed")
    print("Enter 'Fibonacci' for Fibonacci")
    print("Enter 'Palindrome' for Palindrome")
    print("Enter 'Factorial' for Factorial")

    choice = input("\nEnter the choice : ")

    if choice == 'Armstrong':
        num = int(input("Enter a number : "))
        originalnum = num
        arm = 0

        while originalnum > 0:
            digit = originalnum % 10
            arm += digit ** 3
            originalnum //= 10

        if num == arm:
            print("\nIt is an Armstrong Number")
        else:
            print("\nIt is not an Armstrong Number")

    elif choice == 'Reversed':
        a = int(input("Enter a number in 'A' : "))
        b = int(input("Enter a number in 'B' : "))

        a = a + b
        b = a - b
        a = a - b

        print(f"\nThe value in 'A' :  {a}")
        print(f"The value in 'B' :  {b}")

    elif choice == 'Factorial':
        num = int(input("Enter a number : "))
        fact = 1
        for i in range(1, num + 1):
            fact *= i

        print(f"\nThe factorial of {num} is {fact}")

    elif choice == 'Fibonacci':
        num = int(input("Enter a number : "))
        a = 0
        b = 1

        for i in range(num):
            print(a)
            temp = a
            a = b
            b += temp

    elif choice == 'Palindrome':
        num = int(input("Enter a number: "))
        originalnum = num
        palin = 0

        while num > 0:
            digit = num % 10
            palin = palin * 10 + digit
            num //= 10

        if originalnum == palin:
            print(f"\n{originalnum} is a Palindrome number!!")
        else:
            print(f"\n{originalnum} is not a Palindrome number!!")

    take = input("\nDo you want to continue (yes or stop) : ")
    if take.lower() == 'stop':
        print("\nProgram terminated")
        break
