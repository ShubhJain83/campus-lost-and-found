from lost_items import report_lost_item, view_lost_items
from found_items import report_found_item, view_found_items
from matching import find_possible_matches
from reports import view_statistics, view_my_reports
from storage import load_records, update_record_status
from utils import print_header, pause, get_int


def search_items(records):
    print_header("SEARCH ITEMS")

    keyword = input(
        "Enter keyword (or press Enter to skip): "
    ).strip().lower()

    category = input(
        "Enter category (or press Enter to skip): "
    ).strip().lower()

    location = input(
        "Enter location (or press Enter to skip): "
    ).strip().lower()

    results = []

    for item in records:

        text = (
            f"{item.get('name', '')} "
            f"{item.get('description', '')}"
        ).lower()

        if keyword and keyword not in text:
            continue

        if category and category != item.get(
            "category", ""
        ).lower():
            continue

        if location and location not in item.get(
            "location", ""
        ).lower():
            continue

        results.append(item)

    if not results:
        print("\nNo matching records found.")

    else:
        for item in results:
            print_item(item)

        print(f"\nTotal results: {len(results)}")

    pause()


def print_item(item):
    print("-" * 55)
    print(f"ID          : {item['id']}")
    print(f"Type        : {item['type'].title()}")
    print(f"Item        : {item['name']}")
    print(f"Category    : {item['category'].title()}")
    print(f"Description : {item['description']}")
    print(f"Location    : {item['location']}")
    print(f"Date        : {item['date']}")
    print(f"Contact     : {item['contact']}")
    print(f"Status      : {item['status'].title()}")


def manage_status(records):
    print_header("MANAGE ITEM STATUS")

    item_id = input(
        "Enter item ID: "
    ).strip()

    item = next(
        (x for x in records if x["id"] == item_id),
        None
    )

    if not item:
        print("\nItem ID not found.")
        pause()
        return

    print_item(item)

    print("\n1. Mark as Returned")
    print("2. Mark as Unresolved")
    print("3. Cancel")

    choice = input("Choose: ").strip()

    if choice == "1":

        update_record_status(
            item_id,
            "returned"
        )

        print("\nItem marked as returned.")

    elif choice == "2":

        update_record_status(
            item_id,
            "unresolved"
        )

        print("\nItem marked as unresolved.")

    else:
        print("\nNo changes made.")

    pause()


def main():

    while True:

        records = load_records()

        print_header(
            "CAMPUS LOST & FOUND MANAGEMENT SYSTEM"
        )

        print("1. Report Lost Item")
        print("2. Report Found Item")
        print("3. View Lost Items")
        print("4. View Found Items")
        print("5. Search Items")
        print("6. Find Possible Matches")
        print("7. View My Reports")
        print("8. Manage Item Status")
        print("9. View Campus Statistics")
        print("10. Exit")

        choice = get_int(
            "Enter your choice: ",
            1,
            10
        )

        if choice == 1:
            report_lost_item()

        elif choice == 2:
            report_found_item()

        elif choice == 3:
            view_lost_items()

        elif choice == 4:
            view_found_items()

        elif choice == 5:
            search_items(records)

        elif choice == 6:
            find_possible_matches(records)

        elif choice == 7:
            view_my_reports(records)

        elif choice == 8:
            manage_status(records)

        elif choice == 9:
            view_statistics(records)

        elif choice == 10:
            print(
                "\nThank you for using "
                "Campus Lost & Found Management System."
            )
            break


if __name__ == "__main__":
    main()