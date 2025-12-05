from lib.models.vendor import Vendor
from lib.database.config import get_session

def vendor_menu(user):
    session = get_session()

    while True:
        print("\n--- Vendor Management ---")
        print("1. Add Vendor")
        print("2. View Vendors")
        print("3. Update Vendor")
        print("4. Delete Vendor")
        print("5. Book Vendor")
        print("6. Return to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_vendor(session)
        elif choice == "2":
            view_vendors(session)
        elif choice == "3":
            update_vendor(session)
        elif choice == "4":
            delete_vendor(session)
        elif choice == "5":
            book_vendor(session)
        elif choice == "6":
            break
        else:
            print("Invalid choice, try again.")

def add_vendor(session):
    print("\n--- Add Vendor ---")
    name = input("Vendor Name: ")
    service_type = input("Service Type (DJ, Catering, Photography, etc): ")
    cost = float(input("Cost: "))

    vendor = Vendor(name=name, service_type=service_type, cost=cost)
    session.add(vendor)
    session.commit()

    print(f"Vendor '{name}' added successfully.")

def view_vendors(session):
    print("\n--- Vendor List ---")
    vendors = session.query(Vendor).all()

    if not vendors:
        print("No vendors found.")
        return

    for v in vendors:
        status = "BOOKED" if v.is_booked else "AVAILABLE"
        print(f"ID: {v.id} | {v.name} | {v.service_type} | Cost: ${v.cost} | {status}")

def update_vendor(session):
    vendor_id = input("Enter Vendor ID to update: ").strip()
    vendor = session.query(Vendor).filter_by(id=vendor_id).first()

    if not vendor:
        print("Vendor not found.")
        return

    print(f"Updating vendor: {vendor.name}")
    vendor.name = input(f"New Name [{vendor.name}]: ") or vendor.name
    vendor.service_type = input(f"Service Type [{vendor.service_type}]: ") or vendor.service_type
    new_cost = input(f"Cost [{vendor.cost}]: ")
    vendor.cost = float(new_cost) if new_cost else vendor.cost

    session.commit()
    print("Vendor updated successfully.")

def delete_vendor(session):
    vendor_id = input("Enter Vendor ID to delete: ").strip()
    vendor = session.query(Vendor).filter_by(id=vendor_id).first()

    if not vendor:
        print("Vendor not found.")
        return

    session.delete(vendor)
    session.commit()

    print(f"Vendor '{vendor.name}' deleted successfully.")

def book_vendor(session):
    vendor_id = input("Enter Vendor ID to book: ").strip()
    vendor = session.query(Vendor).filter_by(id=vendor_id).first()

    if not vendor:
        print("Vendor not found.")
        return

    if vendor.is_booked:
        print("This vendor is already booked.")
        return

    vendor.is_booked = True
    session.commit()

    print(f"Vendor '{vendor.name}' successfully booked!")
