"""
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers
"""

# number which user've entered
num=121

# convert that number into string
num_str=str(num)
reversed_num_str=num_str[::-1]
print("reversed number is ",reversed_num_str)

# convert that number into integer again
num_int=int(reversed_num_str)

# check if original number and reversed number are same or not
if num==num_int:
    print("Number is palindrome")
else:
    print("Number is not palindrome")


# if both are same then palindrome else not palindrome