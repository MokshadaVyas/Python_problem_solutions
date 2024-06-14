"""
Check if a value exists in a dictionary 
"""

# Define a dictionary with keys and their corresponding values
dict = {
    "a": "Computer Engineering",
    "b": "Data Science",  # Fixed capitalization for consistency
    "c": "Web Development",  # Fixed spelling of "Development"
    "d": "Mechanical Engineering"
}

# Define the target value we are looking for in the dictionary values
target_value = "Data Science"

# Check if the target value is in the values of the dictionary
if target_value in dict.values():
    # If found, print that the target value is in the dictionary
    print(target_value, "is in the dictionary")
else:
    # If not found, print "Not found"
    print("Not found")
