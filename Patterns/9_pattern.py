"""
    *    
   ***   
  *****  
 ******* 
*********
"""

nums_rows=5

for i in range(1,nums_rows+1):
    for j in range(nums_rows-i):
        print(" ",end='')
    for j in range(2*i-1):
        print("*",end='')
    for j in range(nums_rows-i):
        print(" ",end='')
    print()
