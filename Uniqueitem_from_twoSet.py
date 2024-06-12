"""
Get Only unique items from two sets
Write a Python program to return a new set with unique items from both sets by removing duplicates.
"""

set1={100,200,300,400,500}
set2={400,500,600,700,200}

set3=set1|set2
print(set3)