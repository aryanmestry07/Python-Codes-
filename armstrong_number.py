# Armstrong Number Program

def is_armstrong(num: int) -> bool:
    """Check if a number is an Armstrong number."""
    original_num = num
    arm = 0

    while num > 0:
        digit = num % 10
        arm += digit ** 3
        num //= 10

    return original_num == arm


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if is_armstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
