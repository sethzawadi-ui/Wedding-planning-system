from lib.cli.guests_cli import guest_menu
from lib.cli.vendors_cli import vendor_menu
from lib.cli.events_cli import event_menu

def main_menu():
    while True:
        print("\n--- Wedding Planner Main Menu ---")
        print("1. Guests")
        print("2. Vendors")
        print("3. Events")
        print("4. Exit")

        choice = input("Choose one: ").strip()

        if choice == "1":
            guest_menu(None)
        elif choice == "2":
            vendor_menu(None)
        elif choice == "3":
            event_menu(None)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid input.")
