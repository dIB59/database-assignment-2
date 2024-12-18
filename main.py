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


def main():
    logged_in = False
    show_login_screen()
    user_decision = user_input.get_login_screen_decision()

    while not logged_in:
        match user_decision:
            case "q":
                break
            case "1":
                user = user_service.login()
                if user:
                    logged_in = True
            case "2":
                user_service.register()

    while logged_in:
        show_logged_in_menu()
        user_decision = user_input.get_logged_in_screen_decision()
        match user_decision:
            case "1":
                print()
            case "2":
                print()
            case "3":
                print()
            case "4":
                print()


if __name__ == "__main__":
    main()
