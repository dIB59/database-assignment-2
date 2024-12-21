from typing import List

from user import User, NewUser


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


def collect_user_register_data() -> NewUser:
    fname = input("Enter your first name: ").strip()
    lname = input("Enter your last name: ").strip()
    address = input("Enter your address: ").strip()
    city = input("Enter your city: ").strip()

    while True:
        zip_code = input("Enter your zip code: ").strip()
        if zip_code.isdigit():
            break
        print("Invalid zip code. It must be digits only.")

    # Validate phone number (example validation: must be digits and 10 characters long)
    while True:
        phone = input("Enter your phone number: ").strip()
        if phone.isdigit() and len(phone) == 10:
            break
        print("Invalid phone number. It must be 10 digits long.")

    # Validate email (simple validation)
    email = __get_email()

    # Validate password (example validation: at least 8 characters)
    password = __get_password()

    new_user = NewUser(fname, lname, address, city, zip_code, phone, email, password)

    return new_user


def get_login_data():
    return __get_email(), __get_password()


def __get_email():
    while True:
        email = input("Enter your email: ").strip()
        if __is_valid_email(email):
            break
        print("Invalid email address. Please enter a valid email.")
    return email


def __is_valid_email(email: str):
    if "@" not in email and "." not in email:
        return False
    if email.count("@") > 1:
        return False
    if email.index(".") < email.index("@"):
        return False
    if email.index("@") == 0 or email.index(".") == len(email) - 1:
        return False
    if email.index(".") - email.index("@") == 1:
        return False
    return True


def __get_password():
    while True:
        password = input("Enter your password: ").strip()
        if len(password) >= 8:
            break
        print("Password must be at least 8 characters long.")
    return password


def get_browse_subject_decision(subjects: List):
    return __validate_user_input(
        "Type in your option: ", [str(i) for i in range(len(subjects))]
    )


def get_login_screen_decision():
    return __validate_user_input("Type in your option: ", ["1", "2", "q"])


def get_logged_in_screen_decision():
    return __validate_user_input("Type in your option: ", ["1", "2", "3", "4"])


if __name__ == "__main__":
    collect_user_register_data()


def get_pagination_decision():
    return input("Type in your option: ")


def get_quantity():
    return __validate_user_input(
        "Enter quantity: ",
        [str(i) for i in range(1, 11)],
        "Invalid quantity. Please try again.",
    )
