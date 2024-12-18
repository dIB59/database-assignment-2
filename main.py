import register
import user_input


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


def login_user():
    print("login user")


def register_user():
    print("register user")


def main():
    exit_p = False

    while not exit_p:
        show_login_screen()
        user_decision = user_input.get_login_screen_decision()

        match user_decision:
            case 'q':
                break
            case '1':
                login_user()
            case '2':
                register_user()


if __name__ == '__main__':
    main()
