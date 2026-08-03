my_tasks = []

while True: 
    print(f"===== To-Do List =====\n 1.Add task;\n 2.Delete task;\n 3.Show to-do-list;\n 4.Exit;\n")
    i = int(input("Choose an option:"))
    
    if i==1:
        task = input("Enter the task: ")
        my_tasks.append(task)
        print("The task added successfully!")
    elif i==2:
        if len(my_tasks)==0:
            print("No task to delete.")
        else:
            task = input("Enter the task to delete: ")
            if task in my_tasks:
                my_tasks.remove(task)
                print("The task deleted successfully!")
            else:
                print("The task is not found.")
    elif i==3:
        if len(my_tasks)==0:
            print("To-do list is empty.")
        else:
            print("Your to-do list for today: ")
            for task in my_tasks:
                print(task)
    elif i==4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")