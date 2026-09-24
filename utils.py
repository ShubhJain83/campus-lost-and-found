import uuid


def print_header(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def pause():
    input("\nPress Enter to continue...")


def get_int(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))

            if minimum <= value <= maximum:
                return value

            print(f"Please enter a number between {minimum} and {maximum}.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_id(prefix):
    return f"{prefix}-{uuid.uuid4().hex[:6].upper()}"