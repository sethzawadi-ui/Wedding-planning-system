from datetime import datetime
from lib.models.event import Event
from lib.models.vendor import Vendor
from lib.database.config import get_session

def event_menu(user):
    session = get_session()

    while True:
        print("\n--- Event Management ---")
        print("1. Create Event")
        print("2. View Events")
        print("3. Update Event")
        print("4. Delete Event")
        print("5. Assign Vendor to Event")
        print("6. View Event Vendors")
        print("7. Return to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_event(session)
        elif choice == "2":
            view_events(session)
        elif choice == "3":
            update_event(session)
        elif choice == "4":
            delete_event(session)
        elif choice == "5":
            assign_vendor(session)
        elif choice == "6":
            view_event_vendors(session)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Try again.")


def create_event(session):
    print("\n--- Create New Event ---")
    name = input("Event Name: ")
    date_input = input("Event Date (YYYY-MM-DD): ")
    time_input = input("Event Time (HH:MM): ")
    location = input("Event Location: ")

    date_obj = datetime.strptime(date_input, "%Y-%m-%d").date()
    time_obj = datetime.strptime(time_input, "%H:%M").time()

    event = Event(name=name, date=date_obj, time=time_obj, location=location)
    session.add(event)
    session.commit()

    print(f"Event '{name}' created successfully!")


def view_events(session):
    print("\n--- Event List ---")
    events = session.query(Event).all()

    if not events:
        print("No events found.")
        return

    for e in events:
        print(f"ID: {e.id} | {e.name} | {e.date} {e.time} | {e.location}")


def update_event(session):
    event_id = input("Enter Event ID to update: ").strip()
    event = session.query(Event).filter_by(id=event_id).first()

    if not event:
        print("Event not found.")
        return

    print(f"Updating Event: {event.name}")

    event.name = input(f"New Name [{event.name}]: ") or event.name
    new_date = input(f"New Date [{event.date}] (YYYY-MM-DD): ")
    new_time = input(f"New Time [{event.time}] (HH:MM): ")
    event.location = input(f"New Location [{event.location}]: ") or event.location

    if new_date:
        event.date = datetime.strptime(new_date, "%Y-%m-%d").date()
    if new_time:
        event.time = datetime.strptime(new_time, "%H:%M").time()

    session.commit()
    print("Event updated successfully.")


def delete_event(session):
    event_id = input("Enter Event ID to delete: ").strip()
    event = session.query(Event).filter_by(id=event_id).first()

    if not event:
        print("Event not found.")
        return

    session.delete(event)
    session.commit()
    print("Event deleted successfully.")


def assign_vendor(session):
    print("\n--- Assign Vendor to Event ---")
    vendor_id = input("Vendor ID: ").strip()
    event_id = input("Event ID: ").strip()

    vendor = session.query(Vendor).filter_by(id=vendor_id).first()
    event = session.query(Event).filter_by(id=event_id).first()

    if not vendor:
        print("Vendor not found.")
        return

    if not event:
        print("Event not found.")
        return

    vendor.event = event
    vendor.is_booked = True
    session.commit()

    print(f"Vendor '{vendor.name}' booked for event '{event.name}'.")


def view_event_vendors(session):
    print("\n--- View Vendors Assigned to an Event ---")
    event_id = input("Event ID: ").strip()

    event = session.query(Event).filter_by(id=event_id).first()

    if not event:
        print("Event not found.")
        return

    print(f"\nVendors for Event: {event.name}")

    if not event.vendors:
        print("No vendors assigned to this event.")
        return

    for v in event.vendors:
        print(f"{v.name} | {v.service_type} | Cost: ${v.cost}")

