# Student = {
#     "name":"Rajan",
#     "Age":21,
#     "Marks":91
# }

# print(type(Student))
# print(Student)



#=====================================================================

# Tareeka 1: Curly Braces (Sabse zyada use hone wala)
student = {
    "name": "Rajan",
    "age": 21,
    "course": "Python",
    "marks": 85,
    "city":"Lucknow",
}

# # Access - Modify
# print(student["name"])

# print(student.get("age"))


#UPDATE 

# student["marks"] = 80
# student["course"] = "DSA"

# print(student)

# pop() method key ko hata ke uski value deta hai
student.pop("city")

# del statement se direct delete
del student["age"]

print(student)
