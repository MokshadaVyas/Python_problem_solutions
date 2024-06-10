"""
Turn every item of a list into its square
Given a list of numbers. write a program to turn every item of a list into its square.
"""
# method-1

list1=[1,2,3,4,5,6,7,8,9,10]

def square(numbers):
    list2=[]
    for i in list1:
        list2.append(pow(i,2))
    return list2


print("Square of these number is ",square(list1))

# Method-2

list=[10,20,30,40,50]

def square(numbers):
    list2=[]
    for i in list:
        list2.append(i*i)
    return list2

print("Square of these numbers: ",square(list))