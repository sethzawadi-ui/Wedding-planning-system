from lib.models.budget import Budget
from lib.models.expense import Expense
from lib.models.vendor import Vendor
from lib.models.event import Event
from lib.database.config import get_session

def budget_menu(user):
    session = get_session()

    while True:
        print("\n--- Budget Management ---")
        print("1. Set Total Budget")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. View Budget Summary")
        print("5. Return to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            set_total_budget(session)
        elif choice == "2":
            add_expense(session)
        elif choice == "3":
            view_expenses(session)
        elif choice == "4":
            view_budget_summary(session)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def set_total_budget(session):
    total = input("Enter total wedding budget: $").strip()
    try:
        total = float(total)
    except ValueError:
        print("Invalid input. Must be a number.")
        return

    budget = session.query(Budget).first()
    if not budget:
        budget = Budget(total_budget=total)
        session.add(budget)
    else:
        budget.total_budget = total
    session.commit()
    print(f"Total budget set to ${total}")


def add_expense(session):
    budget = session.query(Budget).first()
    if not budget:
        print("Set a total budget first.")
        return

    description = input("Expense description: ")
    amount_input = input("Amount: $").strip()
    try:
        amount = float(amount_input)
    except ValueError:
        print("Amount must be a number.")
        return

    event_id = input("Event ID (optional, press Enter to skip): ").strip()
    vendor_id = input("Vendor ID (optional, press Enter to skip): ").strip()

    event = session.query(Event).filter_by(id=event_id).first() if event_id else None
    vendor = session.query(Vendor).filter_by(id=vendor_id).first() if vendor_id else None

    expense = Expense(description=description, amount=amount, budget=budget, event=event, vendor=vendor)
    session.add(expense)
    session.commit()

    print(f"Added expense '{description}' of ${amount}")


def view_expenses(session):
    budget = session.query(Budget).first()
    if not budget or not budget.expenses:
        print("No expenses found.")
        return

    print("\n--- Expenses ---")
    for exp in budget.expenses:
        print(exp)


def view_budget_summary(session):
    budget = session.query(Budget).first()
    if not budget:
        print("No budget set.")
        return

    print("\n--- Budget Summary ---")
    print(f"Total Budget: ${budget.total_budget}")
    spent = sum(exp.amount for exp in budget.expenses)
    print(f"Total Spent: ${spent}")
    print(f"Remaining: ${budget.remaining_budget()}")
