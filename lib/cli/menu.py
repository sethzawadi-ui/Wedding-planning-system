from database.config import SessionLocal
from models.budget import Budget
from models.expense import Expense

session = SessionLocal()

def create_budget():
    try:
        total = float(input("Enter total wedding budget amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    budget = Budget(total_budget=total)
    session.add(budget)
    session.commit()
    print(f"Budget of {total} created successfully!")

def add_expense():
    budgets = session.query(Budget).all()
    if not budgets:
        print("No budgets found. Please create a budget first.")
        return

    print("Available budgets:")
    for b in budgets:
        print(f"{b.id}: Total - {b.total_budget}, Remaining - {b.calculate_remaining()}")

    try:
        budget_id = int(input("Select budget ID to add expense to: "))
        budget = session.query(Budget).filter_by(id=budget_id).first()
        if not budget:
            print("Invalid budget ID.")
            return
    except ValueError:
        print("Invalid input.")
        return

    name = input("Enter expense name: ")
    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    budget.add_expense(name, amount)
    session.commit()
    print(f"Added expense '{name}' of amount {amount} to budget {budget.id}.")

def view_budget():
    budgets = session.query(Budget).all()
    if not budgets:
        print("No budgets found.")
        return

    for b in budgets:
        print(f"\nBudget ID: {b.id}")
        print(f"Total: {b.total_budget}")
        print(f"Remaining: {b.calculate_remaining()}")
        print("Expenses:")
        for e in b.expenses:
            print(f"  - {e.name}: {e.amount}")

def main_menu():
    while True:
        print("\n--- Wedding Planner Main Menu ---")
        print("1. Manage Budget")
        print("2. Add Expense")
        print("3. View Budget")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_budget()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_budget()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
