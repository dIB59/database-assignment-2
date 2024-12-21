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


def handle_browse_subject(user, database, user_input):
    subjects = sorted(database.get_book_subjects())
    _display_subjects(subjects)

    subject_index = user_input.get_browse_subject_decision(subjects)
    chosen_subject = subjects[int(subject_index) - 1]

    _browse_books_by_subject(user, chosen_subject, database, user_input)


def handle_search_by_author_title(user, database, user_input):
    while True:
        search_option = user_input.get_search_by_author_title_decision()
        if search_option == "1":
            author = input("Enter author name: ")
            _search_books_by_author(user, author, database, user_input)
        elif search_option == "2":
            title = input("Enter title: ")
            _search_books_by_title(user, title, database, user_input)
        elif search_option == "":
            break
        else:
            print("Invalid option. Please try again.")


def _browse_books_by_subject(user, subject, database, user_input):
    books = database.get_books_by_subject(subject)
    _paginate_and_add_to_cart(user, books, database, user_input, f"Books for subject: {subject}")


def _search_books_by_author(user, author, database, user_input):
    books = database.get_books_by_author(author)
    if books:
        _paginate_and_add_to_cart(user, books, database, user_input, f"Books by author: {author}")
    else:
        print("No books found for the author.")


def _search_books_by_title(user, title, database, user_input):
    books = database.get_books_by_title(title)
    if books:
        _paginate_and_add_to_cart(user, books, database, user_input, f"Books with title: {title}")
    else:
        print("No books found for the title.")


def _paginate_and_add_to_cart(user, books, database, user_input, context_message):
    books_per_page = 2
    total_books = len(books)
    current_page = 0

    while True:
        displayed_books = _get_books_for_page(books, current_page, books_per_page)

        print(f"\n{context_message}")
        _print_books(displayed_books)

        _display_pagination_options(current_page, total_books, books_per_page)
        user_choice = user_input.get_pagination_decision()

        if user_choice.lower() == "":
            break
        elif user_choice.lower() == "n" and (current_page + 1) * books_per_page < total_books:
            current_page += 1
        elif user_choice.lower() == "p" and current_page > 0:
            current_page -= 1
        elif database.get_book_by_isbn(user_choice):
            _add_book_to_cart(user, user_choice, database, user_input)
        else:
            print("Invalid choice. Please try again.")


def _add_book_to_cart(user, book_isbn, database, user_input):
    quantity = user_input.get_quantity()
    database.add_to_cart(user.user_id, book_isbn, quantity)
    cart = database.get_cart(user.user_id)

    print("\nBooks in your cart:")
    _print_books(cart)
    input("Press Enter to continue")


def _display_subjects(subjects):
    print("\nAvailable Subjects:")
    for idx, subject in enumerate(subjects):
        print(f"{idx + 1}. {subject}")


def _get_books_for_page(books, current_page, books_per_page):
    start_index = current_page * books_per_page
    end_index = start_index + books_per_page
    return books[start_index:end_index]


def _display_pagination_options(current_page, total_books, books_per_page):
    print("\nOptions:")
    print("Enter the ISBN of the book to add to cart")
    if current_page > 0:
        print("P - Previous Page")
    if (current_page + 1) * books_per_page < total_books:
        print("N - Next Page")
    print("Press Enter to go back to the menu")


def _print_books(books):
    if books:
        for book in books:
            print(f"{book}")  # Customize this as per book attributes
    else:
        print("No books to display.")


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
            if user_decision == "2":
                handle_search_by_author_title(user)
            elif user_decision == "3":
                #handle_check_out(user)
                print("cej")
            elif user_decision == "4":
                user = None
            else:
                handle_logged_in_menu_option(user_decision)


if __name__ == "__main__":
    main()
