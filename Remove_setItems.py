"""
Remove items from the set at once
Write a Python program to remove items 10, 20, 30 from the following set at once.
"""

set1={10,20,30,40,50,60,70,80,90,100}
set1.difference_update({10, 20, 30})
print(set1)