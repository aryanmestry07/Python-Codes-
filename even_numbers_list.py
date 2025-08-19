# Program that takes a list of numbers and returns a new list with only the even numbers

def get_even_numbers(numbers):
    """Return a list of even numbers from the given list."""
    return [num for num in numbers if num % 2 == 0]


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original list:", numbers)
    print("Even numbers:", get_even_numbers(numbers))
