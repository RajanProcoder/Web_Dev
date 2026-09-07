        # f.write("I am Rajan \n")
        # f.write("I am Great \n")
        # f.write("I am Fine \n")
        # f.write("I am Nice \n")
        # f.write("I am Lucknow ")

# Step 1: File mein student ke naam add karna (Append mode)
# def add_student(name):
#     with open("attendance.txt", "a") as file:
#         file.write(name + "\n")
#     print(f"{name} ko list mein add kar diya gaya hai.")

# Step 2: Sabhi students ke naam print karna (Readlines mode)
# def show_all_students():
#     try:
#         with open("attendance.txt", "r") as file:
#             students = file.readlines()
            
#             print("\n--- Attendance List ---")
#             for index, student in enumerate(students, 1):
#                 # .strip() ka use '\n' ko hatane ke liye hota hai
#                 print(f"{index}. {student.strip()}")
                
#     except FileNotFoundError:
#         print("Abhi tak koi file nahi bani hai! Pehle student add karo.")

# # --- DRY RUN BENCH ---
# add_student("Rajan")
# add_student("Vikas")
# show_all_students()