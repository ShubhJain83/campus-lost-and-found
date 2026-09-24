from collections import Counter

from utils import print_header, pause


def view_statistics(records):
    print_header("CAMPUS STATISTICS")

    total = len(records)

    lost = sum(
        1 for item in records
        if item["type"] == "lost"
    )

    found = sum(
        1 for item in records
        if item["type"] == "found"
    )

    returned = sum(
        1 for item in records
        if item["status"] == "returned"
    )

    unresolved = sum(
        1 for item in records
        if item["status"] == "unresolved"
    )

    print(f"Total reports : {total}")
    print(f"Lost reports  : {lost}")
    print(f"Found reports : {found}")
    print(f"Returned      : {returned}")
    print(f"Unresolved    : {unresolved}")

    # Category statistics
    categories = Counter(
        item["category"]
        for item in records
    )

    print("\nItems by category:")

    if categories:
        for category, count in categories.most_common():
            print(f"- {category.title()}: {count}")
    else:
        print("No category data available.")

    # Location statistics
    locations = Counter(
        item["location"]
        for item in records
    )

    print("\nReports by location:")

    if locations:
        for location, count in locations.most_common():
            print(f"- {location}: {count}")
    else:
        print("No location data available.")

    pause()


def view_my_reports(records):
    print_header("VIEW MY REPORTS")

    contact = input(
        "Enter the contact information used in your report: "
    ).strip().lower()

    results = [
        item for item in records
        if item["contact"].lower() == contact
    ]

    if not results:
        print("No reports found for this contact.")

    else:
        for item in results:
            print("-" * 55)
            print(f"ID      : {item['id']}")
            print(f"Type    : {item['type'].title()}")
            print(f"Item    : {item['name']}")
            print(f"Date    : {item['date']}")
            print(f"Status  : {item['status'].title()}")

        print(f"\nTotal reports: {len(results)}")

    pause()