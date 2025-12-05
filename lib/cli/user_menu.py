# CLI for managing users in the Wedding Planning System
# Allows adding, viewing, updating, and deleting users with role management

from models.user import User
import getpass

class UserMenu:
    def __init__(self):
        self.user_model = User()
        self.current_user = None

    def display_menu(self):
        print("\nUser Menu:")
        print("1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Login")
        print("6. Logout")
        print("7. Back to Main Menu")

    def add_user(self):
        name = input("Enter full name: ")
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        role = input("Enter role (Admin, Planner, Bride, Groom, Guest): ")

        if role not in User.ROLES:
            print(f"Invalid role. Must be one of: {', '.join(User.ROLES)}")
            return

        user = User(name=name, username=username)
        user.set_password(password)
        user.role = role
        user.save()
        print(f"User '{username}' with role '{role}' added successfully.")

    def view_users(self):
        users = self.user_model.all()
        if not users:
            print("No users found.")
            return
        for u in users:
            print(f"ID: {u.id}, Name: {u.name}, Username: {u.username}, Role: {u.role}")

    def update_user(self):
        user_id = input("Enter User ID to update: ")
        user = self.user_model.get_by_id(user_id)
        if not user:
            print(f"User ID {user_id} not found.")
            return

        name = input(f"Enter new name [{user.name}]: ") or user.name
        username = input(f"Enter new username [{user.username}]: ") or user.username
        role = input(f"Enter new role [{user.role}]: ") or user.role

        if role not in User.ROLES:
            print(f"Invalid role. Must be one of: {', '.join(User.ROLES)}")
            return

        user.name = name
        user.username = username
        user.role = role
        user.save()
        print(f"User ID {user_id} updated successfully.")

    def delete_user(self):
        user_id = input("Enter User ID to delete: ")
        user = self.user_model.get_by_id(user_id)
        if not user:
            print(f"User ID {user_id} not found.")
            return

        user.delete()
        print(f"User ID {user_id} deleted successfully.")

    def login(self):
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        user = self.user_model.authenticate(username, password)
        if user:
            self.current_user = user
            print(f"Login successful! Welcome {user.name} ({user.role}).")
        else:
            print("Invalid username or password.")

    def logout(self):
        if self.current_user:
            print(f"User {self.current_user.username} logged out.")
            self.current_user = None
        else:
            print("No user currently logged in.")
