"""
12345
1234
123
12
1
"""

num_rows=5

for i in range(1,num_rows+1):
    for j in range(1,num_rows-i+2):
        print(j,end='')
    print()