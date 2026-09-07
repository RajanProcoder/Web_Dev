
account = {
    "name": "Rajan",
    "pin": "903121",
    "balance": 1000
}

password = input("Enter ATM Pin Number: ")

# 1. Correct PIN check using variable name
if account["pin"] == password:
    print(f"\nCorrect PIN! Welcome {account['name']} Brother 🎉\n")

    # 2. Loop sirf tabhi chalega jab PIN sahi hoga
    while True:
        print("||=============================================||")
        print(" 1. Check Balance")
        print(" 2. Deposit")
        print(" 3. Withdraw")
        print(" 4. Exit")
        print("||=============================================||")

        choice = input("Enter Your Choice (1-4): ")

        if choice == "1":
            print(f"\n💰 Current Balance is: ₹{account['balance']}\n")

        elif choice == "2":
            deposit = int(input("Enter Deposit Amount: ₹"))
            account["balance"] += deposit
            print(f"✅ ₹{deposit} successfully deposited! New Balance: ₹{account['balance']}\n")

        elif choice == "3":
            withdraw = int(input("Enter Withdraw Amount: ₹"))
            # `>=` use kiya taaki poora balance bhi nikaal sakein
            if account["balance"] >= withdraw:
                account["balance"] -= withdraw
                print(f"💵 Please collect ₹{withdraw}. Remaining Balance: ₹{account['balance']}\n")
            else:
                print("❌ Insufficient Balance! Aapke pass itne paise nahi hain.\n")

        elif choice == "4":
            print("\nThank You Brother! Have a great day! 🙏")
            break
        else:
            print("⚠️ Invalid Choice! Please enter between 1 and 4.\n")

else:
    print("\n❌ Sorry, Wrong PIN! Try Again.")