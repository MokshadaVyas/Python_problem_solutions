"""
Create a string made of the first, middle and last character
Write a program to create a new string made of an input string’s first, middle, and last character.
"""

# print the original string
str="alice"
print("Original string is",str)

# get the first element of the string
first_letter=str[0]

#calculate length of the string
l=len(str)

#find middle element of the string
m=int(l/2)
mid_letter=str[m]

#get the last element of the string
last_letter=str[l-1]

#Create a new string by concatenating the first, middle, and last elements
result=first_letter+mid_letter+last_letter
print("New string is",result)