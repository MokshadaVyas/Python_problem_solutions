"""
write a program that calculate student's marks and percentage
"""


name = input("Enter name of the student: ")
print("--Please enter marks of all the subjects--")
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

total_marks = m1 + m2 + m3 + m4 + m5
average = total_marks / 5

total_possible_marks = 500
max_marks_per_subject = 100

percentage = (total_marks / total_possible_marks) * 100

print(f"{name} got {percentage:.2f}%")
