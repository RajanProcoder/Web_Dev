
# ==========================================
# PROJECT: STUDENT RECORD MANAGEMENT SYSTEM
# ==========================================

# FILE NAME DHAN MEIN RAKHEIN
FILE_NAME = "student_data.txt"


# ------------------------------------------
# FUNCTION 1: NAYA STUDENT ADD KARNA
# ------------------------------------------
def add_student():
    print("\n--- NAYA STUDENT ADD KAREIN ---")
    roll_no = input("Roll Number darj karein: ")
    name = input("Student Ka Naam darj karein: ")
    marks = input("Marks darj karein: ")

    # 'a' (Append) mode ka use kar rahe hain taaki purana data delete na ho
    with open(FILE_NAME, "a") as file:
        # Data ko comma (,) se jod kar line ke end mein '\n' lagakar likhte hain
        file.write(f"{roll_no},{name},{marks}\n")

    print(f"✅ {name} ka record safaltapoorvak save ho gaya!")


# ------------------------------------------
# FUNCTION 2: SABHI STUDENTS KO DEKHNA
# ------------------------------------------
def view_all_students():
    print("\n--- SABHI STUDENTS KA RECORD ---")

    try:
        # 'r' (Read) mode mein file khol rahe hain
        with open(FILE_NAME, "r") as file:

            # Check karne ke liye ki file khali toh nahi hai
            lines = file.readlines()
            if not lines:
                print("⚠️ File khali hai! Koi record nahi mila.")
                return

            print("Roll No\t|\tNaam\t|\tMarks")
            print("-" * 35)

            # File ki har line par loop chala rahe hain
            for line in lines:
                # 1. .strip() se line ke end ka '\n' aur extra spaces hataya
                clean_line = line.strip()

                # 2. .split(",") se comma par string ko tukdon mein toda (List banayi)
                # "101,Rajan,85" -> ['101', 'Rajan', '85']
                data = clean_line.split(",")

                roll_no = data[0]
                name = data[1]
                marks = data[2]

                # Data ko properly formatting ke saath screen par print kar rahe hain
                print(f"{roll_no}\t|\t{name}\t|\t{marks}")

    except FileNotFoundError:
        # Agar file pehle se exist nahi karti toh ye error handle hoga
        print("⚠️ File exist nahi karti! Pehle koi record add karein.")


# ------------------------------------------
# FUNCTION 3: STUDENT SEARCH KARNA (BY ROLL NO)
# ------------------------------------------
def search_student():
    print("\n--- STUDENT SEARCH KAREIN ---")
    search_roll = input("Search karne ke liye Roll Number dalein: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            # Directly file object par loop chalayein (Memory Efficient Way)
            for line in file:
                clean_line = line.strip()  # '\n' hataya
                data = clean_line.split(",")  # Data tod kar list banayi

                # Check karte hain ki match mila ya nahi
                if data[0] == search_roll:
                    print("\n✅ RECORD MIL GAYA!")
                    print(f"Roll No : {data[0]}")
                    print(f"Naam    : {data[1]}")
                    print(f"Marks   : {data[2]}")
                    found = True
                    break  # Record milne par loop rok do

            if not found:
                print(
                    f"❌ Roll Number {search_roll} ka koi record nahi mila."
                )

    except FileNotFoundError:
        print("⚠️ Record file abhi bani hi nahi hai!")


# ------------------------------------------
# MAIN MENU LOOP
# ------------------------------------------
def main():
    while True:
        print("\n=============================")
        print(" STUDENT MANAGEMENT SYSTEM ")
        print("=============================")
        print("1. Naya Student Add Karein")
        print("2. Sabhi Students Dekhein")
        print("3. Student Search Karein")
        print("4. Exit (Bahar Niklein)")

        choice = input("Apna option chunein (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("\nDhanyawad Rajan bhai! Program band ho raha hai.")
            break
        else:
            print("❌ Sahi option chunein (1 se 4 ke beech).")


# Program yahan se start hoga
main()