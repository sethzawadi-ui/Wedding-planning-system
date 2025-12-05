# CLI for managing tasks in the Wedding Planning System
# Allows creation, viewing, updating, and marking tasks as complete

from models.task import Task
from models.user import User
from datetime import datetime

class TaskMenu:
    def __init__(self):
        self.task_model = Task()
        self.user_model = User()

    def display_menu(self):
        print("\nTask Menu:")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Complete")
        print("5. Back to Main Menu")

    def create_task(self):
        name = input("Enter task name: ")
        description = input("Enter description: ")
        assigned_to = input("Assign to (username): ")
        due_date_str = input("Enter due date (YYYY-MM-DD): ")

        # Validate due_date
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Task not created.")
            return

        # Check if user exists
        if not self.user_model.exists(assigned_to):
            print(f"User '{assigned_to}' does not exist.")
            return

        task = Task(name=name, description=description, assigned_to=assigned_to, due_date=due_date)
        task.save()
        print(f"Task '{name}' created and assigned to '{assigned_to}'.")

    def view_tasks(self):
        tasks = self.task_model.all()
        if not tasks:
            print("No tasks found.")
            return
        for t in tasks:
            status = "Complete" if t.completed else "Pending"
            print(f"ID: {t.id}, Name: {t.name}, Assigned to: {t.assigned_to}, Due: {t.due_date}, Status: {status}")

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        task = self.task_model.get_by_id(task_id)
        if not task:
            print(f"Task ID {task_id} not found.")
            return

        name = input(f"Enter new name [{task.name}]: ") or task.name
        description = input(f"Enter new description [{task.description}]: ") or task.description
        due_date_str = input(f"Enter new due date (YYYY-MM-DD) [{task.due_date}]: ") or str(task.due_date)

        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Update canceled.")
            return

        task.name = name
        task.description = description
        task.due_date = due_date
        task.save()
        print(f"Task ID {task_id} updated successfully.")

    def mark_complete(self):
        task_id = input("Enter Task ID to mark complete: ")
        task = self.task_model.get_by_id(task_id)
        if not task:
            print(f"Task ID {task_id} not found.")
            return
        task.completed = True
        task.save()
        print(f"Task '{task.name}' marked as complete.")
