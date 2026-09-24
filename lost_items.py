from storage import load_records, add_record
from validators import (
    validate_non_empty,
    validate_date,
    validate_contact,
    validate_category
)
from utils import print_header, pause, generate_id


def report_lost_item():
    print_header("REPORT LOST ITEM")

    try:
        name = validate_non_empty(
            input("Item name: "),
            "Item name"
        )

        category = validate_category(
            input("Category: ")
        )

        description = validate_non_empty(
            input("Description: "),
            "Description"
        )

        location = validate_non_empty(
            input("Last seen location: "),
            "Location"
        )

        item_date = validate_date(
            input("Date lost (YYYY-MM-DD): ")
        )

        contact = validate_contact(
            input("Contact information: ")
        )

        record = {
            "id": generate_id("L"),
            "type": "lost",
            "name": name,
            "category": category,
            "description": description,
            "location": location,
            "date": item_date,
            "contact": contact,
            "status": "unresolved"
        }

        add_record(record)

        print("\nLost item reported successfully!")
        print(f"Your Item ID is: {record['id']}")

    except ValueError as error:
        print(f"\nError: {error}")

    pause()


def view_lost_items():
    print_header("LOST ITEMS")

    records = [
        item for item in load_records()
        if item["type"] == "lost"
    ]

    if not records:
        print("No lost item reports available.")

    else:
        for item in records:
            print("-" * 55)
            print(f"ID          : {item['id']}")
            print(f"Item        : {item['name']}")
            print(f"Category    : {item['category'].title()}")
            print(f"Location    : {item['location']}")
            print(f"Date Lost   : {item['date']}")
            print(f"Status      : {item['status'].title()}")

    pause()