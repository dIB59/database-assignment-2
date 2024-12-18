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





if __name__ == "__main__":
    main()
