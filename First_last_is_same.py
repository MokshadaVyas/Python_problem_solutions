"""
Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
"""

# Define the list
list1 = [10, 20, 30, 40, 50, 10]
print("Given list is:", list1)

# Get the length of the list (though it's not used in the function)
n = len(list1)

# Define the function to check if the first and last elements are the same
def first_last_same(x):
    # Loop over each element in the list (though the loop is not necessary for this check)
    for i in list1:
        # Check if the first element is the same as the last element
        if x[0] == x[-1]:
            return True
        else:
            return False

# Print the result of the function
print(first_last_same(list1))
