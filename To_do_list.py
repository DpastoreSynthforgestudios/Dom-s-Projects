print("Welcome to Your To-Do List Manager")

tasks = []

# Function to display tasks with numbering
def display_tasks():
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

# Load tasks from file
try:
    with open("tasks.txt", "r") as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    # If the file doesn't exist, start with an empty task list
    tasks = []

while True:
    user_input = input(
        "Please choose an option: \n1. Add a task \n2. View all tasks \n3. Mark task as done \n4. Delete a task \n5. Exit \n> ")

    # Add a task
    if user_input == '1':
        add_task = input("Enter the task description: ")
        tasks.append(add_task)
        print("Task added successfully!")

    # View all tasks
    elif user_input == '2':
        if tasks:
            print("Here are your current tasks:")
            display_tasks()
        else:
            print("No tasks available.")

    # Mark task as done
    elif user_input == '3':
        if tasks:
            display_tasks()
            mark_task = input("Enter the number of the task to mark as done: ")
            if mark_task.isdigit() and 1 <= int(mark_task) <= len(tasks):
                task_index = int(mark_task) - 1
                tasks[task_index] += " - [Done]"
                print(f"Task {mark_task} marked as done!")
            else:
                print("Invalid task number.")
        else:
            print("No tasks available to mark as done.")

    # Delete a task
    elif user_input == '4':
        if tasks:
            display_tasks()
            delete_task = input("Enter the number of the task to delete: ")
            if delete_task.isdigit() and 1 <= int(delete_task) <= len(tasks):
                task_index = int(delete_task) - 1
                deleted_task = tasks.pop(task_index)
                print(f"Task '{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number.")
        else:
            print("No tasks available to delete.")

    # Exit
    elif user_input == '5':
        # Save tasks to file before exiting
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Goodbye!")
        break

    # Invalid input handling
    else:
        print("Invalid option. Please enter a number between 1 and 5.")
