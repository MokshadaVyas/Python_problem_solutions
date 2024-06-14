"""
55555
5555
555
55
5
"""
nums_rows=5
num=nums_rows

for i in range(1,nums_rows+1):
    for j in range(nums_rows-i+1):
        print(num,end='')
    print()