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
    exit_p = False

    while not exit_p:
        show_login_screen()
        user_decision = input("WHAT DO YOU WANT TO DO?")

        if user_decision == "q":
            break


if __name__ == '__main__':
    main()
