from lib.cli.menu import main_menu
from lib.database.config import init_db

def run():
    # Initialize the database tables
    init_db()
    # Launch the main CLI menu
    main_menu()

if __name__ == "__main__":
    run()
