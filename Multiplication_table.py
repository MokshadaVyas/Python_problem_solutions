"""
Write multiplication table of given number
"""

num=int(input("Which number's multiplication table do you want? "))

print(f"Here is your multiplication table for {num}")
for i in range(1,11):
    total=num*i
    print(f"{num}*{i}={total}")