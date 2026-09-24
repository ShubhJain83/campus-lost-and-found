from storage import load_records, add_record
from validators import (
    validate_non_empty,
    validate_date,
    validate_contact,
    validate_category
)
from utils import print_header, pause, generate_id


def report_found_item():
    print_header("REPORT FOUND ITEM")

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
            input("Found location: "),
            "Location"
        )

        item_date = validate_date(
            input("Date found (YYYY-MM-DD): ")
        )

        contact = validate_contact(
            input("Contact information: ")
        )

        record = {
            "id": generate_id("F"),
            "type": "found",
            "name": name,
            "category": category,
            "description": description,
            "location": location,
            "date": item_date,
            "contact": contact,
            "status": "unresolved"
        }

        add_record(record)

        print("\nFound item reported successfully!")
        print(f"Your Item ID is: {record['id']}")

    except ValueError as error:
        print(f"\nError: {error}")

    pause()


def view_found_items():
    print_header("FOUND ITEMS")

    records = [
        item for item in load_records()
        if item["type"] == "found"
    ]

    if not records:
        print("No found item reports available.")

    else:
        for item in records:
            print("-" * 55)
            print(f"ID          : {item['id']}")
            print(f"Item        : {item['name']}")
            print(f"Category    : {item['category'].title()}")
            print(f"Location    : {item['location']}")
            print(f"Date Found  : {item['date']}")
            print(f"Status      : {item['status'].title()}")

    pause()