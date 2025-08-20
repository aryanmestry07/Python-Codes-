# Program to count vowels and consonants in a given string

def count(word): 
    vowels = 'aeiouAEIOU'
    
    v_count = 0
    c_count = 0

    # Loop through each character in the word
    for char in word:
        # Check if the character is a letter (ignore digits/symbols)
        if char.isalpha():
            if char in vowels:
                v_count += 1   # Increment vowel counter
            else:
                c_count += 1   # Increment consonant counter
    
    print("Vowels:", v_count)
    print("Consonants:", c_count)
    print()

# Take user input
user_word = input("Enter a string: ")

# Call the function
count(user_word)
