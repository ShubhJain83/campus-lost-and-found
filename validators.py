from datetime import datetime


def validate_non_empty(value, field_name):
    value = value.strip()

    if not value:
        raise ValueError(f"{field_name} cannot be empty.")

    return value


def validate_date(value):
    value = value.strip()

    try:
        datetime.strptime(value, "%Y-%m-%d")
        return value

    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")


def validate_contact(value):
    value = value.strip()

    if not value:
        raise ValueError("Contact information cannot be empty.")

    if len(value) < 3:
        raise ValueError("Contact information is too short.")

    return value


def validate_category(value):
    allowed_categories = [
      "electronics", "documents", "clothing", "accessories",
"books", "keys", "stationery", "bags", "other"
    ]

    value = value.strip().lower()

    if value not in allowed_categories:
        raise ValueError(
            "Invalid category. Choose from: "
            + ", ".join(allowed_categories)
        )

    return value