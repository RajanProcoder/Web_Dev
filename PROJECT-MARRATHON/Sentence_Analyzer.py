import random

# Student dict jisme subjects aur unke random marks hain
student_marks = {
    "Maths": random.randint(40, 100),
    "Science": random.randint(40, 100),
    "English": random.randint(40, 100),
    "Hindi": random.randint(40, 100),
}

print("=== STUDENT REPORT CARD ===")

total_marks = 0

# Loop chala kar har subject ka mark dikhayenge aur total karenge
for subject, marks in student_marks.items():
    print(f"{subject}: {marks}")
    total_marks += marks

# Average calculate karna
average = total_marks / len(student_marks)

print("---------------------------")
print(f"Total Marks: {total_marks} / 400")
print(f"Percentage: {average:.2f}%")

# Grade decide karna
if average >= 75:
    print("Grade: A (Distinction!)")
elif average >= 60:
    print("Grade: B")
else:
    print("Grade: C")
