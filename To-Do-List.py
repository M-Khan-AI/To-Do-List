
# To-Do List
# Project 1 - Python Programming

# Store all tasks in a list
tasks = []

while True:

    # Display menu
    print("\n===== TO-DO LIST =====")
    print(" Add Task")
    print(" View Tasks")
    print(" Update Task")
    print(" Delete Task")
    print(" Exit")

    # Get user's choice
    choice = input("Enter your choice: ")

    # -------------------------
    # 1. ADD TASK
    # -------------------------
    if choice == "add":

        task = input("Enter your task: ")

        tasks.append(task)

        print("Task added successfully!")


    # -------------------------
    # 2. VIEW TASKS
    # -------------------------
    elif choice == "view":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")


    # -------------------------
    # 3. UPDATE TASK
    # -------------------------
    elif choice == "update":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_number = int(input("Enter task number to update: "))

                if 1 <= task_number <= len(tasks):

                    new_task = input("Enter the new task: ")

                    tasks[task_number - 1] = new_task

                    print("Task updated successfully!")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")


    # -------------------------
    # 4. DELETE TASK
    # -------------------------
    elif choice == "delete":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_number = int(input("Enter task number to delete: "))

                if 1 <= task_number <= len(tasks):

                    deleted_task = tasks.pop(task_number - 1)

                    print(f"Task '{deleted_task}' deleted successfully!")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")


    # -------------------------
    # 5. EXIT
    # -------------------------
    elif choice == "exit":

        print("Goodbye!")
        break


    # -------------------------
    # INVALID CHOICE
    # -------------------------
    else:

        print("Invalid choice. Please select 1-5.")
