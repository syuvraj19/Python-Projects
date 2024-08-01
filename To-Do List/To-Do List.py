def add_task(task_list, task):
    task_list.append(task)
    print("Task added!")

def remove_task(task_list, task):
    if task in task_list:
        task_list.remove(task)
        print("Task removed!")
    else:
        print("Task not found!")

def view_tasks(task_list):
    if task_list:
        print("Your tasks:")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks found!")

def todo_list_app():
    task_list = []

    print("Welcome to the To-Do List Application!")
    
    while True:
        print("\n1. Add a task")
        print("2. Remove a task")
        print("3. View all tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task_list, task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task_list, task)
        elif choice == '3':
            view_tasks(task_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    todo_list_app()
