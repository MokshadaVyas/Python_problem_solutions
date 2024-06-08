# taking number from user
num=int(input("Enter number: "))

# function to find factorial number
def factorial(n):
    # 0 and 1 factorial number is 1
    if(n==0 or n==1):   
        return 1
    else:
        return n*factorial(n-1)
    
# Display output
print("Factorial of the number is",factorial(num))