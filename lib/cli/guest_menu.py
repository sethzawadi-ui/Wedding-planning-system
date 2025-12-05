# File: cli/guest_menu.py

from models.guest import Guest
from database.config import Session
from datetime import datetime

session = Session()

def add_guest():
    """Add a new guest to the database."""
    name = input("Enter guest name: ").strip()
    email = input("Enter guest email: ").strip()
    phone = input("Enter guest phone: ").strip()
    rsvp = input("Has guest RSVPed? (yes/no): ").strip().lower() == "yes"

    new_guest = Guest(
        name=name,
        email=email,
        phone=phone,
        rsvp=rsvp,
        created_at=datetime.now()
    )
    session.add(new_guest)
    session.commit()
    print(f"Guest '{name}' added successfully!")

def view_guests():
    """View all guests."""
    guests = session.query(Guest).all()
    if not guests:
        print("No guests found.")
        return
    print("\nGuest List:")
    for guest in guests:
        status = "RSVPed" if guest.rsvp else "Not RSVPed"
        print(f"ID: {guest.id} | Name: {guest.name} | Email: {guest.email} | Phone: {guest.phone} | Status: {status}")

def update_guest():
    """Update guest details."""
    guest_id = input("Enter guest ID to update: ").strip()
    guest = session.query(Guest).filter_by(id=guest_id).first()
    if not guest:
        print("Guest not found.")
        return

    print("Leave blank to keep current value.")
    name = input(f"Name ({guest.name}): ").strip()
    email = input(f"Email ({guest.email}): ").strip()
    phone = input(f"Phone ({guest.phone}): ").strip()
    rsvp_input = input(f"RSVP (yes/no) ({'yes' if guest.rsvp else 'no'}): ").strip().lower()

    if name:
        guest.name = name
    if email:
        guest.email = email
    if phone:
        guest.phone = phone
    if rsvp_input in ["yes", "no"]:
        guest.rsvp = rsvp_input == "yes"

    session.commit()
    print(f"Guest ID {guest_id} updated successfully!")

def delete_guest():
    """Delete a guest."""
    guest_id = input("Enter guest ID to delete: ").strip()
    guest = session.query(Guest).filter_by(id=guest_id).first()
    if not guest:
        print("Guest not found.")
        return

    session.delete(guest)
    session.commit()
    print(f"Guest ID {guest_id} deleted successfully!")

def guest_menu():
    """CLI menu for guest management."""
    while True:
        print("\n--- Guest Management ---")
        print("1. Add Guest")
        print("2. View Guests")
        print("3. Update Guest")
        print("4. Delete Guest")
        print("5. Back to Main Menu")

        choice = input("Select an option: ").strip()
        if choice == "1":
            add_guest()
        elif choice == "2":
            view_guests()
        elif choice == "3":
            update_guest()
        elif choice == "4":
            delete_guest()
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")
