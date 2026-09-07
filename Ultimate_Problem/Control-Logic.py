print("--------------------------------")
print("Network Company Billing:")

Free = int(input("Enter your Time in Min: "))

# 1. Base Bill Calculate Karo
if Free >= 0 and Free <= 100:
    Total_Bill = 0

elif Free > 100 and Free <= 200:
    extra_min = Free - 100  # Pehle 100 free the
    Total_Bill = extra_min * 1

else:
    extra_min = Free - 200
    # Pehle 100 free + Agle 100 min ka ₹100 + Baki extra min ka ₹2/min
    Total_Bill = 100 + (extra_min * 2)

# 2. Tax / Surcharge Rule (Ye sabhi slabs ke liye lag sakta hai)
if Total_Bill > 150:
    tax = Total_Bill * 0.20  # 20% tax
    Total_Bill = Total_Bill + tax  # Tax bill mein add kar diya

print(f"Total Final Amount is: ₹{Total_Bill}")