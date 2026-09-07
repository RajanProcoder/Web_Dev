tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Apna option chuno (1-4): ")

    if choice == "1":
        enter_task = input("Enter your task: ")
        tasks.append(enter_task)
        print("Task Added Successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("Abhi koi task nahi hai!")
        else:
            print("\n--- AAPKE TASKS ---")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("Delete karne ke liye koi task nahi hai!")
        else:
            delete_num = int(input("Delete karne ke liye Task Number daalein: "))
            
            # Check kar rahe hain ki user ne valid number dala hai ya nahi
            if 1 <= delete_num <= len(tasks):
                removed = tasks.pop(delete_num - 1)
                print(f"'{removed}' delete ho gaya!")
            else:
                print("Galat task number!")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Fir se try karo.")