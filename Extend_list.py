"""
Create a new list from two list using the following condition
Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
"""

# function for merge two list
def merge_list(list1,list2):
    # list3 is an empty list
    list3=[]
    # add all odd numbers in list3
    for num in list1:
        if num%2==1:
            list3.append(num)
    # add all even numbers in list3
    for num in list2:
        if num%2==0:
            list3.append(num)

    # return list3
    return list3

# Given list   
list1=[10,20,25,30,35]
list2=[40,45,60,75,90]

# call the function and print the result
print(merge_list(list1,list2))