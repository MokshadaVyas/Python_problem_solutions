"""
11111
2222
333
44
5
"""


nums_rows=5

for i in range(1,nums_rows+1):
    for j in range(nums_rows-i+1):
        print(i,end='')
    print()