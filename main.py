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


def main():

    show_login_screen()
    user_decision = user_input.get_login_screen_decision()

    match user_decision:
        case "q":
            return
        case "1":
            user_service.login()
        case "2":
            user_service.register()


if __name__ == "__main__":
    main()
