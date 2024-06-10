"""
Calculate the sum of all numbers from 1 to n given number
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to n given number
"""

# method-1
num=int(input("Enter number: "))
sum=0
for i in range(1,num+1):
        sum+=i

print("Sum is:",sum)

# method-2
num=int(input("Enter number:"))

for i in range(1,num+1):
        total=((num)*(num+1))//2
print("Sum is:",total) 


    
