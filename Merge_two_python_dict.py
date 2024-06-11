"""
Merge two Python dictionaries into one
"""


# Define the first dictionary with personal information
dict1 = {"name": "John", "age": 18, "city": "Usa"}

# Define the second dictionary with marks
dict2 = {"mark1": 70, "mark2": 82, "mark3": 96}

# Print the original dictionaries
print("Original dictionaries are\n", dict1, dict2)

# Create a copy of the first dictionary to avoid modifying the original
dict3 = dict1.copy()

# Update the copy with the contents of the second dictionary
dict3.update(dict2)

# Print the updated dictionary
print("Updated dictionary is\n", dict3)
