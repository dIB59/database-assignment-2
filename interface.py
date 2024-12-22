from datetime import datetime, timedelta
from typing import Dict, List

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


#This option should display an invoice (books’ information (ISBN, Title), book price, quantity, and total price) and a question to checkout. The order may have many books, not just one book.
def show_checkout_menu(books: List[Dict]):
    width = 70
    print(f"{'Books in your cart:'.center(width)}")
    print("\n")
    for book in books:
        print(
            f"{'ISBN: ' + book['isbn'] + ' Title: ' + book['title'] + ' Price: $' + str(book['price']) 
               + ' Quantity: ' + str(book['qty']):^{width}}" + 'Total:' + book['price'] * book['qty']
        )
    print("\n")
    total_price = sum([book["price"] * book["qty"] for book in books])
    print(f"{'Total price: $' + str(total_price):^{width}}")
    print("\n")
    print(f"{'Proceed to check out (Y/N)?:'.center(width)}")


# Use the user’s current address for shipping. The order is saved to the Order table with a received date (current
# date), shipment date (generated date one week in a head), with shipment address corresponding to the member’s
# address provided at registration. And to ‘odetails’ table, save the books (isbn), their quantity, and amount (
# quantity * book price).
def show_invoice(user: User, books: List[Dict]):
    width = 70
    print("*" * width)
    print(f"***{'':{width - 6}}***")
    print(f"***{'Welcome to Online Book Store'.center(width - 6)}***")
    print(f"***{'Invoice'.center(width - 6)}***")
    print(f"***{'':{width - 6}}***")
    print("*" * width)
    print("\n")
    print(f"{'Order Details:'.center(width)}")
    print("\n")

    current_date = datetime.now().date()
    shipment_date = current_date + timedelta(days=7)
    print(f"{'Books in your cart:'.center(width)}")
    print("\n")
    for book in books:
        print(
            f"{'ISBN: ' + book['isbn'] + ' Title: ' + book['title'] + ' Price: $' + str(book['price']) + ' Quantity: '
               + str(book['qty']) + 'Total:' + book['price'] * book['qty']:^{width}}")
    print(f"{'Received Date: ' + str(current_date):^{width}}")
    print(f"{'Shipment Date: ' + str(shipment_date):^{width}}")
    print(f"{'Shipment Address: ' + user.address:^{width}}")
    print("\n")
