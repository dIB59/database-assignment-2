def __validate_user_input(
    prompt: str,
    valid_inputs: list[str],
    error_message: str = "Invalid input. Please try again.",
) -> str:
    while True:
        user_input = input(prompt).strip()
        if user_input in valid_inputs:
            return user_input
        print(error_message)


def collect_user_data():
    fname = input("Enter your first name: ").strip()
    lname = input("Enter your last name: ").strip()
    address = input("Enter your address: ").strip()
    city = input("Enter your city: ").strip()

    while True:
        zip_code = input("Enter your zip code: ").strip()
        if zip_code.isdigit():
            break
        print("Invalid zip code. It must be digits only.")

    zip_code = input("Enter your zip code: ").strip()

    # Validate phone number (example validation: must be digits and 10 characters long)
    while True:
        phone = input("Enter your phone number: ").strip()
        if phone.isdigit() and len(phone) == 10:
            break
        print("Invalid phone number. It must be 10 digits long.")

    # Validate email (simple validation)
    while True:
        email = input("Enter your email: ").strip()
        if "@" in email and "." in email:
            break
        print("Invalid email address. Please enter a valid email.")

    # Validate password (example validation: at least 8 characters)
    while True:
        password = input("Enter your password: ").strip()
        if len(password) >= 8:
            break
        print("Password must be at least 8 characters long.")

    return fname, lname, address, city, zip_code, phone, email, password


def get_login_screen_decision():
    return __validate_user_input("Type in your option: ", ["1", "2", "q"])


if __name__ == "__main__":
    collect_user_data()
