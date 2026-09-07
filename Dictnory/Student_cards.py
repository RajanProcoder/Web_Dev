# Initial Data
student = {
    "name": "Rajan",
    "roll_no": 101,
    "marks": {
        "Maths": 85,
        "Science": 90,
        "English": 80
    }
}


total = 0
student["marks"]["English"] = 88

print("Science Marks =",student["marks"]["Science"])

print(student)


for key , value in student["marks"].items():
     total = total + value

print(f"Total Marks is - {total}")





















# print(student["marks"]["Maths"])

# print(student["marks"]["English"])
