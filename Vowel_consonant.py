"""
Check whether the entered string is vowel or consonant
"""
# Prompting the user to enter a string and storing it in the variable 'str'
str = input("Enter string: ")

# Checking if the entered string is a vowel
if str == 'a' or str == 'e' or str == 'i' or str == 'o' or str == 'u':
    print("String is vowel")
else:
    print("String is consonant")
