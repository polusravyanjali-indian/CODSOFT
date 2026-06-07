# CodSoft Task 1 - To Do List
# Created by: Polu Sravyanjali

todos = []

def show_menu():
    print("\n" + "=" * 30)
    print("       TO-DO LIST APP")
    print("=" * 30)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 30)

def add_task():
    task = input("Enter task: ")
    todos.append({"task": task, "status": "Pending"})
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if len(todos) == 0:
        print("No tasks found!")
    else:
        print("\n--- Your Tasks ---")
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo['task']} [{todo['status']}]")

def update_task():
    view_tasks()
    if len(todos) > 0:
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(todos):
            todos[num-1]["status"] = "Completed ✅"
            print("Task marked as completed!")
        else:
            print("Invalid task number!")

def delete_task():
    view_tasks()
    if len(todos) > 0:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(todos):
            removed = todos.pop(num-1)
            print(f"Task '{removed['task']}' deleted!")
        else:
            print("Invalid task number!")

while True:
    show_menu()
    choice = input("Enter choice (1-5): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")