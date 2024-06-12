"""
Return a new set of identical items from two sets
"""

set1={10,20,30,40,50}
set2={30,40,50,60,70}
print("Original set is:",set1,set2)

set3=set1.intersection(set2)

print("Common elements are:",set3)
