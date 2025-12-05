# CLI for managing events in the Wedding Planning System
# Allows creation, viewing, and updating of events

from models.event import Event

class EventMenu:
    def __init__(self):
        self.event_model = Event()

    def display_menu(self):
        print("\nEvent Menu:")
        print("1. Create Event")
        print("2. View Events")
        print("3. Update Event")
        print("4. Back to Main Menu")

    def create_event(self):
        name = input("Enter event name: ")
        date_str = input("Enter event date (YYYY-MM-DD): ")
        location = input("Enter location: ")

        # Validate date format
        from datetime import datetime
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Event not created.")
            return

        event = Event(name=name, date=date, location=location)
        event.save()
        print(f"Event '{name}' scheduled for {date} at {location}.")

    def view_events(self):
        events = self.event_model.all()
        if not events:
            print("No events found.")
            return
        for e in events:
            print(f"ID: {e.id}, Name: {e.name}, Date: {e.date}, Location: {e.location}")

    def update_event(self):
        event_id = input("Enter Event ID to update: ")
        event = self.event_model.get_by_id(event_id)
        if not event:
            print(f"Event ID {event_id} not found.")
            return

        name = input(f"Enter new name [{event.name}]: ") or event.name
        date_str = input(f"Enter new date (YYYY-MM-DD) [{event.date}]: ") or str(event.date)
        location = input(f"Enter new location [{event.location}]: ") or event.location

        # Validate date
        from datetime import datetime
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Update canceled.")
            return

        event.name = name
        event.date = date
        event.location = location
        event.save()
        print(f"Event ID {event_id} updated successfully.")

