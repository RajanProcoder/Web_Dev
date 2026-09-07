# Dictnory

student = {
    "Math" : 40,
    "Phy" : 50,
    "Hindi":50,
    "Eng" : 70,
    "Che" : 34
}

# len of Students

length = len(student)

total = 0
for value in student.values():
    total += value

Avg = (total / length)
print("Total Avg Of Marks :",Avg)
print("Total marks :",total)