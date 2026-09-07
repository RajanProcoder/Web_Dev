
# print("===== Personal Expense Tracker =====")

# Expense_Tracker = []

# while True:
#     print("\n------------------------------")
#     print("1. Add Expense")
#     print("2. View Expense")
#     print("3. Total Kharcha")
#     print("4. Sabse Bada Kharcha")
#     print("5. Filter Expenses (Limit se bade kharche)")
#     print("6. Exit")

#     choice = input("Apna option chuno (1-6): ")

#     # 1. Add Expense
#     if choice == "1":
#         amount = int(input("Enter your Amount in Expenses: ₹"))
#         Expense_Tracker.append(amount)  # Sahi syntax: append()
#         print("Expense Added Successfully!")

#     # 2. View Expenses
#     elif choice == "2":
#         if len(Expense_Tracker) == 0:
#             print("There is No Expense added yet!")
#         else:
#             print("\n--- Aapke Saare Kharche ---")
#             for index, expense in enumerate(Expense_Tracker, start=1):
#                 print(f"{index}. ₹{expense}")

#     # 3. Total Kharcha
#     elif choice == "3":
#         if len(Expense_Tracker) == 0:
#             print("Pehle kharcha add toh karo!")
#         else:
#             Total_Kharcha = sum(Expense_Tracker)
#             print(f"Total Expense is : ₹{Total_Kharcha}")

#     # 4. Sabse Bada Kharcha
#     elif choice == "4":
#         if len(Expense_Tracker) == 0:
#             print("Pehle kharcha add toh karo!")
#         else:
#             Largest_Kharcha = max(Expense_Tracker)
#             print(f"Sabse Bada Kharcha is : ₹{Largest_Kharcha}")

#     # 5. Filter Expenses (List Comprehension Test) 🔥
#     elif choice == "5":
#         if len(Expense_Tracker) == 0:
#             print("Kharcha list khali hai!")
#         else:
#             limit = int(input("Kitni amount se bade kharche dekhne hain? ₹"))
            
#             # LIST COMPREHENSION: Sirf limit se bade kharche ek nayi list mein aayenge
#             filtered = [x for x in Expense_Tracker if x > limit]

#             if len(filtered) == 0:
#                 print(f"₹{limit} se bada koi kharcha nahi hai.")
#             else:
#                 print(f"\n--- ₹{limit} se bade kharche ---")
#                 for item in filtered:
#                     print(f"-> ₹{item}")

#     # 6. Exit
#     elif choice == "6":
#         print("Thank You for using Expense Tracker!")
#         break

#     else:
#         print("Invalid choice! Fir se try karo.")









