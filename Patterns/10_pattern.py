"""
*********
 *******
  *****
   ***
    *
"""
num_rows = 5

for i in range(num_rows):
    # Print leading spaces
    for j in range(i):
        print(" ", end='')
    # Print stars
    for j in range(2 * (num_rows - i) - 1):
        print("*", end='')
    # Move to the next line
    print()
