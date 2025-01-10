from datetime import datetime, timedelta
from typing import Dict, List

from models import User


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
    print('4 Logout'.center(width))


def show_checkout_menu(books: List[Dict]):
    width = 70
    print(f"{'Books in your cart:'.center(width)}")
    print("\n")
    for book in books:
        print(
            f"{'ISBN: ' + book['isbn'] + ' Title: ' + book['title'] + ' Price: €' + str(book['price'])
               + ' Quantity: ' + str(book['qty']):^{width}}"
            + "Total:"
            + book["price"] * book["qty"]
        )
    print("\n")
    total_price = sum([book["price"] * book["qty"] for book in books])
    print(f"{'Total price: €' + str(total_price):^{width}}")
    print("\n")
    print(f"{'Proceed to check out (Y/N)?:'.center(width)}")


def show_invoice(user: User, books: List[Dict], order_number: int):
    width = 100
    title_width = 45

    print("-" * width)
    print(f"\n{f'Invoice for Order no.{order_number}':^{width}}")
    print("-" * width)

    # Order Number
    print(f"{'Order Number:'} {order_number}")
    print("-" * width)

    # Table Header
    print(f"{'ISBN':<15} {'Title':<45} {'Price':>10} {'Qty':>5} {'Total':>10}")
    print("-" * width)

    # Table Rows
    order_total = 0  # Initialize total amount
    for book in books:
        total = book["price"] * book["qty"]
        order_total += total

        # Truncate the title if it exceeds the title_width
        title = book["title"]
        if len(title) > title_width:
            title = title[: title_width - 3] + "..."

        print(
            f"{book['isbn']:<15} {title:<45} {book['price']:>9.2f} {book['qty']:>5} {total:>9.2f}"
        )

    print("-" * width)

    # Order Total Row
    print(f"{'':<80}{'Order Total:':<10} ${order_total:>9.2f}")

    # Summary Section
    print("-" * width)
    print(f"{'Received Date:':<20} {str(datetime.now().date()):<20}")
    print(
        f"{'Shipment Date:':<20} {str((datetime.now() + timedelta(days=7)).date()):<20}"
    )
    print(f"{'User Name:':<20} {user.fname} {user.lname}")
    print(f"{'Shipment Address:':<20} {user.address}, {user.city}, {user.zip}")
    print("-" * width)


def print_books(books):
    max_length = 50  # Maximum length for text before truncating

    def truncate(text, max_len):
        return text if len(text) <= max_len else text[: max_len - 3] + "..."

    if books:
        # Print table header
        header = f"{'Author':<30} {'Title':<50} {'ISBN':<15} {'Price':>8}"
        print(header)
        print("-" * len(header))

        # Print each book's details in a formatted row
        for book in books:
            author = truncate(book["author"], 30)
            title = truncate(book["title"], max_length)
            isbn = truncate(book["isbn"], max_length)
            price = f"${book['price']:>7.2f}"

            print(f"{author:<30} {title:<50} {isbn:<15} {price:>8}")
    else:
        print("No books to display.")
