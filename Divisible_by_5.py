"""
Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5
"""

# Define the list with a different name to avoid conflict with the built-in type
numbers = [10, 45, 96, 85, 41, 25, 5]

# Define the function to print numbers divisible by 5
def divisible():
    # Loop through each element in the list
    for i in numbers:
        # Check if the current element is divisible by 5
        if i % 5 == 0:
            # Print the element if it is divisible by 5
            print(i)

# Call the function
divisible()
