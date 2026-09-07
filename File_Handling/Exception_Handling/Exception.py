# try:
#     num = int(input("Enter a number: "))
#     result = num / 0
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")


#-------------------------------------------

# Example 2: Invalid Input (ValueError)
# try:
#     num = int(input("Enter a Number: "))
#     print("The Number is:", num)
# except ValueError:
#     print("Error: Invalid input. Please enter a valid integer.")



#------------------------------------------

# Multiple Exceptions Handle Karna

# try:
#     num = int(input("Enter a Number:"))
#     num1 = int(input("Enter a Number:"))
#     result = num / num1
#     print("The Result is :", result)


# except ValueError:
#     print("Error Plese Enter a vali Number")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")



#------------------------------------------
# else Block Ka Use

# try:
#     Num = int(input("Enter a Number:"))
#     print("The Number is:", Num)

# except ValueError:
#     print("Error: Invalid input. Please enter a valid integer.")

# else:
#     if(Num % 2 == 0):
#         print("The Number is Even")
#     else:
#         print("The Number is Odd")





#===========================================
# : finally Block Ka Use

# from unittest import result


# try:
#     number = int(input("Enter a Number:"))
#     number1 = int(input("Enter a Number:"))
#     result = number / number1

#     print("The Result is:", result)
#     print("The Number is:", number)
#     print("The Number is:", number1)

# except ValueError:
#     print("Error value Error Try Again Inter integer value")

# except ZeroDivisionError:
#     print("This Is value devision error Dont use Zero for Devide")

# else:
#     if number % 2 == 0:
#         print("The Number is Even")
#     else:
#         print("The Number is Odd Brother")
    
# finally:
#     print("Finnaly Execution ho gaya bhai")





#------Finally---------------------------------

# try:
#     file = open("sample.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("Error: The file 'sample.txt' was not found.")

# finally:
#     print("🔒 Process complete! (Cleanup code yahan chalta hai)")




#-------------------------------------------
# Universal Exception Catch (Exception as e)

# try:
#     a = [1, 2, 3]
#     print(a[5]) # Ye index nahi hai
# except Exception as e:
#     print(f"❌ Kuch to gadbad hui! Error details: {e}")


#-------------------------------------------
# Raising Exception     

# age = -4

# try:
#     if age < 0:
#         raise ValueError("Age cannot be negative!")
# except ValueError as e:
#     print(f"❌ Error: {e}")



#-------------------------------------------

# Dict Example

# user = {"rajan": 25, "sita": 30}

# try:
#     print(user["gita"])  # KeyError
# except KeyError as e:
#     print(f"❌ Error: {e}. Key not found in the dictionary.")


#-------------------------------------------


# try:
#     age = int(input("Enter Your Age: "))
    
#     # ❌ Negative age check try ke andar hi hoga
#     if age <= 0:
#         raise ValueError("Age 0 ya negative nahi ho sakti!")

# except ValueError as e:
#     # 💡 Agar galat text daala YA negative age dali, dono yahan handle ho jayenge
#     print("❌ Error:", e)

# else:
#     # ✅ Else tabhi chalega jab age bilkul sahi integer (positive) hogi
#     print(f"✅ The Age is: {age}")

# finally:
#     # 🔒 Ye block toh hamesha chalega hi chalega!
#     print("🔒 Tum Kuch Bhi kar lo, mujhe to chalna hi padega bhai!")

#---------------------------------------------------------------------------------------------

# try:
#     amount = int(input("Enter Your Amount: "))
#     withdraw = int(input("Enter Withdraw Amount: "))

#     if amount <= 0:
#         raise ValueError("Ammount Should be Positive Enter gain amounter Gratter then zero")

#     if withdraw > amount:
#         raise ValueError("Withdraw Amount is Greater than Your Amount")

# except ValueError as e:
#     print(f"❌ Error: {e}")

# else:
#     print(f"Transcation is {amount -withdraw }")


# finally:
#     print("🔒 Transaction Process Complete! (Cleanup code yahan chalta hai)")