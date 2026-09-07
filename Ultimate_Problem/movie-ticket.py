
print("===== Movie-Tickets =====")
Age = int(input("Enter The Age: "))
Show_Time = int(input("Enter Show Time (in 24hr format): "))

# Step 1: Base Ticket Price (Age ke hisab se)
if Age < 12:
    Ticket = 100
elif Age >= 12 and Age <= 60:
    Ticket = 200
else:
    Ticket = 150

# Step 2: Show Time Discount Check (Subke liye ek sath!)
if Show_Time < 16:
    Ticket = Ticket - 30  # Flat ₹30 minus kar do

print(f"Total Final Price: ₹{Ticket}")