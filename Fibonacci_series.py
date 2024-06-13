"""
Calculate fibonacci sequence of n numbers
"""
# Function to compute Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Taking input from user for number of terms
num = int(input("Enter number of terms: "))

# Printing Fibonacci series
print("Fibonacci series is:")
for i in range(num):
    print(fibonacci(i))  # Calling fibonacci function and printing each term in the series
