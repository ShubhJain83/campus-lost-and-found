from datetime import datetime

from utils import print_header, pause


def date_score(date1, date2):
    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")

        days_difference = abs((d1 - d2).days)

        if days_difference == 0:
            return 10
        elif days_difference <= 2:
            return 8
        elif days_difference <= 7:
            return 5
        elif days_difference <= 30:
            return 2

    except ValueError:
        pass

    return 0


def calculate_match_score(lost, found):
    score = 0

    # Item name
    lost_name = lost["name"].lower()
    found_name = found["name"].lower()

    if lost_name == found_name:
        score += 40
    elif lost_name in found_name or found_name in lost_name:
        score += 25

    # Category
    if lost["category"].lower() == found["category"].lower():
        score += 20

    # Location
    lost_location = lost["location"].lower()
    found_location = found["location"].lower()

    if lost_location == found_location:
        score += 20
    elif (
        lost_location in found_location
        or found_location in lost_location
    ):
        score += 10

    # Date
    score += date_score(lost["date"], found["date"])

    # Description
    lost_words = set(lost["description"].lower().split())
    found_words = set(found["description"].lower().split())

    common_words = lost_words.intersection(found_words)

    if common_words:
        score += 10

    return score


def find_possible_matches(records):
    print_header("POSSIBLE MATCHES")

    lost_items = [
        item for item in records
        if item["type"] == "lost"
        and item["status"] == "unresolved"
    ]

    found_items = [
        item for item in records
        if item["type"] == "found"
        and item["status"] == "unresolved"
    ]

    if not lost_items or not found_items:
        print(
            "You need at least one unresolved lost item "
            "and one unresolved found item."
        )
        pause()
        return

    matches = []

    for lost in lost_items:
        for found in found_items:
            score = calculate_match_score(lost, found)

            if score >= 50:
                matches.append((score, lost, found))

    matches.sort(
        key=lambda match: match[0],
        reverse=True
    )

    if not matches:
        print("No possible matches found.")

    else:
        for score, lost, found in matches:
            print("\n" + "-" * 60)
            print(f"Match Score: {score}/100")
            print(
                f"Lost : {lost['id']} - "
                f"{lost['name']} ({lost['location']})"
            )
            print(
                f"Found: {found['id']} - "
                f"{found['name']} ({found['location']})"
            )
            print(
                "Review the details before marking an item as returned."
            )

    pause()