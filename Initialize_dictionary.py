"""
Initialize dictionary with default values
"""

dict1={
    "employee1":"John",
    "employee2":"Alice",
    "employee3":"Ruby"
}

dict2={
    "Designation":"Devloper",
    "salary":45000
}

# using fromkeys() Keyword

dict3=dict.fromkeys(dict1,dict2)

print(dict3)