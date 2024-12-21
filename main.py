import database
import user_input
import user_service
from user import User


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


def handle_login() -> User | None:
    user = user_service.login()
    if user:
        print(f"Welcome, {user.fname} {user.lname}!")
        return user
    return None


def handle_register():
    if user_service.register():
        print("Registration successful.")
        input("Please press enter to go back to the menu")
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


def __print_books_pretty(books):
    for book in books:
        print(f"Author: {book['author']}")
        print(f"Title: {book['title']}")
        print(f"ISBN: {book['isbn']}")
        print(f"Price: ${book['price']}")
        print()


def handle_browse_subject(user: User):
    subjects = sorted(database.get_book_subjects())
    print("\nAvailable Subjects:")
    for idx, subject in enumerate(subjects):
        print(f"{idx + 1}. {subject}")

    # Get user decision for a subject
    subject_index = user_input.get_browse_subject_decision(subjects)
    chosen_subject = subjects[int(subject_index) - 1]

    # Fetch books for the selected subject
    books = database.get_books_by_subject(chosen_subject)

    # Display books 2 at a time
    books_per_page = 2
    total_books = len(books)
    current_page = 0

    while True:
        # Get the start and end index for books on the current page
        start_index = current_page * books_per_page
        end_index = start_index + books_per_page
        displayed_books = books[start_index:end_index]

        print(f"\nBooks for subject: {chosen_subject}")
        __print_books_pretty(displayed_books)

        print("\nOptions:")
        print("Enter the ISBN of the book to add to cart")
        if current_page > 0:
            print("P - Previous Page")
        if end_index < total_books:
            print("N - Next Page")
        print("Press Enter to go back to the menu")

        user_choice = user_input.get_pagination_decision()

        if user_choice.lower() == "":
            break
        elif user_choice.lower() == "n" and end_index < total_books:
            current_page += 1
        elif user_choice.lower() == "p" and current_page > 0:
            current_page -= 1
        elif user_choice.isdigit():
            book_isbn = user_choice
            quantity = user_input.get_quantity()
            database.add_to_cart(user.user_id, book_isbn, quantity)
            print(
                f"Added {quantity} of {books[int(book_isbn) - 1]['title']}"
                f" with ISBN {books[int(book_isbn) - 1]['isbn']} to cart."
            )
        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        user = None

        while not user:
            show_login_screen()
            user_decision = user_input.get_login_screen_decision()
            if user_decision == "q":
                exit("Exiting the program.")
            elif user_decision == "1":
                user = handle_login()
            elif user_decision == "2":
                handle_register()
            else:
                print("Invalid option.")

        while user:
            show_logged_in_menu()
            user_decision = user_input.get_logged_in_screen_decision()
            if user_decision == "1":
                handle_browse_subject(user)
            elif user_decision == "4":
                user = None
            else:
                handle_logged_in_menu_option(user_decision)


if __name__ == "__main__":
    main()
