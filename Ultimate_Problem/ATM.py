
time_slot = int(input("Enter Time"))

if time_slot>=0 and time_slot<=2:
    money = 0
elif time_slot>=3 and time_slot<=5:
    dis = time_slot - 2
    money = dis * 20

else:
    dis = time_slot - 5

    money = 60 + ( dis * 50)


    if money > 300:
        money = 300


print(f"Total Amount is :{money}")
