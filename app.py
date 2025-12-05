# Entry point for the Wedding Planner CLI Application

from lib.cli.menu import main_menu
from lib.database.config import init_db

if __name__ == "__main__":
    print("Initializing database...")
    init_db()
    print("Database ready.\n")

    main_menu()
