# Menu-driven calculator program with addition, subtraction, multiplication, division, and modulus

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b


if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    while True:
        print("\nMenu")
        print("Enter 'add' for addition")
        print("Enter 'sub' for subtraction")
        print("Enter 'mul' for multiplication")
        print("Enter 'div' for division")
        print("Enter 'mod' for modulus")

        choice = input("\nEnter your choice: ").lower()

        if choice == 'add':
            print(f"\n{num1} + {num2} = {add(num1, num2)}")
        elif choice == 'sub':
            print(f"\n{num1} - {num2} = {sub(num1, num2)}")
        elif choice == 'mul':
            print(f"\n{num1} x {num2} = {mul(num1, num2)}")
        elif choice == 'div':
            print(f"\n{num1} / {num2} = {div(num1, num2)}")
        elif choice == 'mod':
            print(f"\n{num1} % {num2} = {mod(num1, num2)}")
        else:
            print("\nEnter a valid choice from the Menu!!")

        take = input("\nDo you want to continue (yes or stop): ").lower()
        if take == 'stop':
            print("\nProgram terminated!!")
            break
