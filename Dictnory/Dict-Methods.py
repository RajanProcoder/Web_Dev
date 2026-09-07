user = {
    "name":"rajan",
    "role":"Developer",
    "level":"Beginners"
}

# for key in user:
#     print(f" {key} :{user[key]}")
    #   print(f"{key}")



# key and value Both Loop

# for key , value in user.items():
#     print(f"{key} : {value}")






# Mini Project student management system
# Mini Project: Student Management System

# 1. Dictionary ka setup
students_db = {
    "Rajan": {"age": 21, "marks": 88},
    "Amit": {"age": 22, "marks": 75},
    "Priya": {"age": 20, "marks": 92}
}

print("=== Student Record System ===")

# 2. Naya Student Add karna
students_db["Sohan"] = {"age": 21, "marks": 80}

# 3. Saare Students ki details display karna
print("\n--- Student Details ---")
for name, info in students_db.items():
    print(f"Naam: {name} | Umar: {info['age']} | Marks: {info['marks']}")

# 4. Average Marks Calculate karna
total_marks = 0
for info in students_db.values():
    total_marks += info["marks"]

avg_marks = total_marks / len(students_db)
print(f"\nClass ka Average Marks: {avg_marks:.2f}")