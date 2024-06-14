"""
Find Maximum and Minimum of two numbers in Python
"""

 
# Prompt the user to enter the numbers
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))

# Print the four numbers entered by the user
print("Four numbers are:", a, b, c, d)

# Find the maximum number among the four
ans1 = max(a, b, c, d)

# Find the minimum number among the four
ans2 = min(a, b, c, d)

# Print the maximum number
print("Maximum number is:", ans1)

# Print the minimum number
print("Minimum number is:", ans2)
