# Palindrome Number Program

def is_palindrome(num: int) -> bool:
    """Check if a number is a Palindrome."""
    original_num = num
    palin = 0

    while num > 0:
        digit = num % 10
        palin = palin * 10 + digit
        num //= 10

    return original_num == palin


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if is_palindrome(number):
        print(f"{number} is a Palindrome number.")
    else:
        print(f"{number} is not a Palindrome number.")
