# cli/task_menu.py

from models.task import Task
from database.config import Session

# Task menu function
def task_menu():
    """CLI menu for managing tasks."""
    session = Session()
    while True:
        print("\n--- Task Management ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Complete")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Task name: ")
            description = input("Description: ")
            assigned_to = input("Assign to user: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            task = Task(
                name=name,
                description=description,
                assigned_to=assigned_to,
                due_date=due_date,
                completed=False
            )
            session.add(task)
            session.commit()
            print(f"Task '{name}' added successfully!")

        elif choice == "2":
            tasks = session.query(Task).all()
            if tasks:
                for t in tasks:
                    status = "Complete" if t.completed else "Pending"
                    print(f"[{t.id}] {t.name} - {status} - Assigned to: {t.assigned_to} - Due: {t.due_date}")
            else:
                print("No tasks found.")

        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            task = session.query(Task).get(task_id)
            if task:
                task.name = input(f"New name ({task.name}): ") or task.name
                task.description = input(f"New description ({task.description}): ") or task.description
                task.assigned_to = input(f"New assigned user ({task.assigned_to}): ") or task.assigned_to
                task.due_date = input(f"New due date ({task.due_date}): ") or task.due_date
                session.commit()
                print(f"Task '{task.name}' updated successfully!")
            else:
                print("Task not found.")

        elif choice == "4":
            task_id = input("Enter Task ID to mark as complete: ")
            task = session.query(Task).get(task_id)
            if task:
                task.completed = True
                session.commit()
                print(f"Task '{task.name}' marked as complete!")
            else:
                print("Task not found.")

        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    session.close()
