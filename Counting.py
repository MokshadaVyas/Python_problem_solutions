"""
Count all letters, digits, and special symbols from a given string
"""

def counting(str):
    # Initialize counters for characters, digits, and symbols
    char_count = 0
    digit_count = 0
    symbol_count = 0

    # Iterate through each character in the string
    for i in str:
        # Check if the character is an alphabetic letter
        if i.isalpha():
            char_count += 1
        # Check if the character is a digit
        elif i.isdigit():
            digit_count += 1
        # If it is neither a letter nor a digit, it is a symbol
        else:
            symbol_count += 1

    # Return the counts as a tuple
    return char_count, digit_count, symbol_count

# Define the input string with embedded quotes and special characters
str = "{\"p%4$bs()jk\"}"
print("Original string is", str)

# Call the counting function and unpack the results into separate variables
char_count, digit_count, symbol_count = counting(str)

# Print the counts of characters, digits, and symbols
print("Characters:", char_count, "\nDigits:", digit_count, "\nSymbols:", symbol_count)
