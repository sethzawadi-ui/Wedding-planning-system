import sys
from getpass import getpass
from lib.models import User
from lib.database.config import get_session
from lib.cli.guests_cli import guest_menu
from lib.cli.vendors_cli import vendor_menu
from lib.cli.events_cli import event_menu
from lib.cli.tasks_cli import task_menu
from lib.cli.budget_cli import budget_menu

# Role-based main menu
def main_menu():
    session = get_session()
    print("Welcome to the Wedding Planning System CLI\n")
    
    user = login(session)
    if not user:
        print("Exiting the system...")
        sys.exit(0)

    while True:
        print("\nMain Menu")
        print("1. Manage Guests")
        print("2. Manage Vendors")
        print("3. Manage Events")
        print("4. Manage Tasks")
        print("5. Manage Budget")
        print("6. Logout")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            guest_menu(user)
        elif choice == "2":
            vendor_menu(user)
        elif choice == "3":
            event_menu(user)
        elif choice == "4":
            task_menu(user)
        elif choice == "5":
            budget_menu(user)
        elif choice == "6":
            print(f"Goodbye {user.username}!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# User login
def login(session):
    print("Login")
    username = input("Username: ").strip()
    password = getpass("Password: ").strip()
    
    # Basic password check using stored hash
    user = session.query(User).filter_by(username=username).first()
    if user and user.check_password(password):
        print(f"Welcome, {user.username}! Role: {user.role}")
        return user
    else:
        print("Invalid username or password.")
        return None
