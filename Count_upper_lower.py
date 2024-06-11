"""
Counting upper and lower characters in a given string
"""


# Prompting the user to enter a string
str = str(input("Enter string name:"))

# Printing the entered string
print("Entered string is", str)

# Initializing counters for uppercase and lowercase characters
upper_count = 0
lower_count = 0

# Iterating through each character in the string
for i in str:
    # Checking if the character is uppercase
    if i.isupper():
        upper_count += 1  # Incrementing the uppercase counter
    else:
        lower_count += 1  # Incrementing the lowercase counter

# Printing the number of uppercase characters
print("Upper characters are:", upper_count)

# Printing the number of lowercase characters
print("Lower characters are:", lower_count)
