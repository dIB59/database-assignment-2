import user_input
import user_service


def show_login_screen():
    width = 70
    print("*" * width)
    print(f"***{'':{width - 6}}***")
    print(f"***{'Welcome to the Online Book Store'.center(width - 6)}***")
    print(f"***{'':{width - 6}}***")
    print("*" * width)
    print(f"\n{'1. Member Login'.center(width)}")
    print(f"{'2. New Member Registration'.center(width)}")
    print(f"\n{'q. Quit'.center(width)}")


def show_logged_in_menu():
    width = 70
    print("*" * width)
    print(f"***{'':{width - 6}}***")
    print(f"***{'Welcome to Online Book Store'.center(width - 6)}***")
    print(f"***{'Member Menu'.center(width - 6)}***")
    print(f"***{'':{width - 6}}***")
    print("*" * width)
    print("\n")
    print(f"{'1 Browse by Subject'.center(width)}")
    print(f"{'2 Search by Author/Title'.center(width)}")
    print(f"{'3 Check Out'.center(width)}")
    print(f"{'4 Logout'.center(width)}")


def handle_login():
    user = user_service.login()
    if user:
        print(f"Welcome, {user["fname"]} {user["lname"]}!")
        return True
    return False


def handle_register():
    if user_service.register():
        print("Registration successful.")
    else:
        print("Something went wrong please try again later.")


def handle_logged_in_menu_option(option):
    options = {
        "1": lambda: print("Option 1 selected."),
        "2": lambda: print("Option 2 selected."),
        "3": lambda: print("Option 3 selected."),
        "4": lambda: print("Logging out"),
    }
    action = options.get(option, lambda: print("Invalid option."))
    action()


def main():
    while True:  # Main application loop
        logged_in = False

        # Main menu loop
        while not logged_in:
            show_login_screen()
            user_decision = user_input.get_login_screen_decision()
            main_menu_actions = {
                "q": lambda: exit("Exiting the program."),
                "1": lambda: handle_login(),
                "2": handle_register,
            }
            action = main_menu_actions.get(user_decision, lambda: print("Invalid option."))
            logged_in = action() if user_decision == "1" else logged_in

        # Logged-in menu loop
        while logged_in:
            show_logged_in_menu()
            user_decision = user_input.get_logged_in_screen_decision()
            if user_decision == "4":  # Logout option
                logged_in = False  # Exit logged-in loop
            else:
                handle_logged_in_menu_option(user_decision)


if __name__ == "__main__":
    main()
