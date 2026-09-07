
#============================================
#STUDENT RECORD MANAGEMENT SYSTEM
#============================================

# I HAVE MADE FILE NAME HERE
FILE_NAME = "student_record.txt"

def Add_students():
    print("Add students Here Brother")

    print("=" * 30)
    roll = input("Appna Roll Number Enter Kare: ")
    name = input("Appna name Enter Kare: ")
    pho_No = input("Appna Number Enter Kare: ")
    Stream = input("Appna Stream Enter Kare: ")

    print("=" * 30)

    with open(FILE_NAME, 'a') as file:
        file.write(f"{roll},{name},{pho_No},{Stream}\n")

    print(f"{name} safalta Purvak save ho gaya")


#=====================================
#SHOW KARUNGA DATA KO BHAI MAIN YAHA
#=====================================

def show_students():
    print("Show students Here Brother")
    print("=" * 50)
    print(f"Roll\t|   Name\t|  Phone_Number\t|  stream")
    print("=" * 50)

    try:
        with open(FILE_NAME, 'r') as file:
            lines = file.readlines()

            if not lines:
                print("Bhai File Bilkul Empty[Khali] Hai")
                return

            for line in lines:
                clean_data = line.strip()
                Data = clean_data.split(",")

                if len(Data) < 4:
                    continue

                roll = Data[0]
                name = Data[1]
                pho_No = Data[2]
                stream = Data[3]

                print(f"{roll}\t| {name}\t| {pho_No}\t| {stream}")

    except FileNotFoundError:
        print("File nahi mili. Pehle ek student add karo.")


def Search_Student():
    Search_student = input("Enter Roll Number: ")

    try:
        with open(FILE_NAME, 'r') as file:
            lines = file.readlines()

            if not lines:
                print("File khali hai. Pehle student add karo.")
                return

            for line in lines:
                clean_data = line.strip()
                data = clean_data.split(",")

                if len(data) < 4:
                    continue

                if Search_student == data[0]:
                    print("Student mil gaya:")
                    print(f"Roll Number: {data[0]}")
                    print(f"Name: {data[1]}")
                    print(f"Phone: {data[2]}")
                    print(f"Stream: {data[3]}")
                    return

            print("Koi student nahi mila jiski roll number aapne diya hai.")
    except FileNotFoundError:
        print("File nahi mili. Pehle student add karo.")


def main():
    while True:
        print("-" * 40)
        print("1. Student Add kare:")
        print("2. student Dekhe:")
        print("3. Student Search Kare:")
        print("4. Exit Bahar Jaye")
        print("-" * 40)

        choice = input("Enter Your Choice ")

        if choice == "1":
            Add_students()

        elif choice == "2":
            show_students()

        elif choice == "3":
            Search_Student()

        elif choice == "4":
            print("Program band ho raha hai. Bye!")
            break
        else:
            print("Sorry invalid Number Brother Enter 1-4")


main()