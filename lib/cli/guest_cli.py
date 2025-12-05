from lib.models.guest import Guest
from lib.database.config import get_session

def guest_menu(user):
    session = get_session()
    while True:
        print("\n--- Guest Management ---")
        print("1. Add Guest")
        print("2. View Guests")
        print("3. Update Guest")
        print("4. Delete Guest")
        print("5. Return to Main Menu")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_guest(session)
        elif choice == "2":
            view_guests(session)
        elif choice == "3":
            update_guest(session)
        elif choice == "4":
            delete_guest(session)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# --- CRUD Functions ---
def add_guest(session):
    name = input("Guest Name: ").strip()
    email = input("Guest Email (optional): ").strip()
    phone = input("Guest Phone (optional): ").strip()
    
    guest = Guest(name=name, email=email, phone=phone)
    session.add(guest)
    session.commit()
    print(f"Guest '{name}' added successfully.")

def view_guests(session):
    guests = session.query(Guest).all()
    if not guests:
        print("No guests found.")
        return
    for guest in guests:
        print(f"ID: {guest.id} | Name: {guest.name} | RSVP: {guest.rsvp_status} | Email: {guest.email} | Phone: {guest.phone}")

def update_guest(session):
    guest_id = input("Enter Guest ID to update: ").strip()
    guest = session.query(Guest).filter_by(id=guest_id).first()
    if not guest:
        print("Guest not found.")
        return

    print(f"Updating Guest: {guest.name}")
    guest.name = input(f"New Name [{guest.name}]: ") or guest.name
    guest.email = input(f"New Email [{guest.email}]: ") or guest.email
    guest.phone = input(f"New Phone [{guest.phone}]: ") or guest.phone
    guest.rsvp_status = input(f"RSVP Status [{guest.rsvp_status}]: ") or guest.rsvp_status
    
    session.commit()
    print(f"Guest '{guest.name}' updated successfully.")

def delete_guest(session):
    guest_id = input("Enter Guest ID to delete: ").strip()
    guest = session.query(Guest).filter_by(id=guest_id).first()
    if not guest:
        print("Guest not found.")
        return
    session.delete(guest)
    session.commit()
    print(f"Guest '{guest.name}' deleted successfully.")
