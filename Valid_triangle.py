"""
Write a Python program to input all sides of a triangle and check whether triangle is valid or not.
"""

# Prompting the user to enter the lengths of the triangle sides
t1 = float(input("Enter length of the first triangle: "))
t2 = float(input("Enter length of the second triangle: "))
t3 = float(input("Enter length of the third triangle: "))

# Checking if the given lengths can form a valid triangle
if t1 + t2 > t3 and t2 + t3 > t1 and t3 + t1 > t2:
    print("Triangle is valid")
else:
    print("Triangle is not valid")
