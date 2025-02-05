import mysql.connector as sconnect
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from models import User


def get_connection():
    return sconnect.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root_password",
    )


def get_book_subjects():
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT DISTINCT subject FROM book_store.books")
            subjects = [row["subject"] for row in cursor.fetchall()]
        return subjects
    finally:
        connection.close()


def get_books_by_subject(subject: str):
    with get_connection() as connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM book_store.books WHERE book_store.books.subject = %s", (subject,)
        )
        return cursor.fetchall()


def register_user(
    fname: str,
    lname: str,
    address: str,
    city: str,
    zip: int,
    phone: str,
    email: str,
    password: str,
    connection: PooledMySQLConnection | MySQLConnectionAbstract,
) -> User or None:
    cursor = connection.cursor()
    insert_query = (
        "INSERT INTO book_store.members (fname, lname, address, city, zip, phone, email, password) VALUES "
        "(%s, %s, %s, %s, %s, %s, %s, %s)"
    )
    values = (fname, lname, address, city, zip, phone, email, password)
    cursor.execute(insert_query, values)
    connection.commit()

    user_id = cursor.lastrowid

    select_query = (
        "SELECT * FROM book_store.members WHERE book_store.members.userid = %s"
    )
    cursor.execute(select_query, (user_id,))
    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user


def login_user(
    email: str,
    password: str,
    connection: PooledMySQLConnection | MySQLConnectionAbstract,
) -> User or None:
    cursor = connection.cursor(dictionary=True)
    select_query = """
        SELECT * FROM book_store.members
        WHERE book_store.members.email = %s AND password = %s
    """
    cursor.execute(select_query, (email, password))
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    return User(*user.values()) if user else None


def get_book_by_isbn(isbn: str):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM book_store.books WHERE book_store.books.isbn = %s", (isbn,)
    )
    res = cursor.fetchone()
    connection.close()
    return res


def get_cart(user_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT book_store.books.isbn,"
        " book_store.books.title,"
        " book_store.books.price,"
        " book_store.cart.qty,"
        " books.author "
        "FROM book_store.cart "
        "JOIN book_store.books ON book_store.cart.isbn = book_store.books.isbn "
        "WHERE book_store.cart.userid = %s",
        (user_id,),
    )
    res = cursor.fetchall()
    connection.close()
    return res


def __exists_in_cart(user_id, book_isbn):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM book_store.cart WHERE book_store.cart.userid = %s AND book_store.cart.isbn = %s",
        (user_id, book_isbn),
    )
    res = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return res > 0


def add_to_cart(user_id, book_isbn, quantity):
    connection = get_connection()
    cursor = connection.cursor()
    if __exists_in_cart(user_id, book_isbn):
        cursor.execute(
            "UPDATE book_store.cart SET qty = qty + %s WHERE book_store.cart.userid = %s AND book_store.cart.isbn = %s",
            (quantity, user_id, book_isbn),
        )
        connection.commit()
        cursor.close()
        connection.close()
        return get_cart(user_id)

    insert_query = "INSERT INTO book_store.cart (userid, isbn, qty) VALUES (%s, %s, %s)"
    values = (user_id, book_isbn, quantity)
    cursor.execute(insert_query, values)
    connection.commit()
    cursor.close()
    connection.close()
    return get_cart(user_id)


def get_books_by_author(author):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM book_store.books WHERE book_store.books.author LIKE %s",
        (f"%{author}%",),
    )
    res = cursor.fetchall()
    connection.close()
    return res


def get_books_by_title(title):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM book_store.books WHERE book_store.books.title LIKE %s",
        (f"%{title}%",),
    )
    res = cursor.fetchall()
    connection.close()
    return res


if __name__ == "__main__":
    s = get_book_subjects()

    book_isbn = get_books_by_subject(s[0])[0]["isbn"]

    print(add_to_cart(1, book_isbn, 2))


def create_order(user_id, cart):
    connection = get_connection()
    cursor = connection.cursor()

    # Fetch the user's address
    fetch_address_query = (
        "SELECT address, city, zip " "FROM book_store.members " "WHERE userid = %s"
    )
    cursor.execute(fetch_address_query, (user_id,))
    member_address = cursor.fetchone()

    if not member_address:
        raise ValueError("User not found or address not available")

    ship_address, ship_city, ship_zip = member_address

    insert_order_query = (
        "INSERT INTO book_store.orders (userid, created, shipAddress, shipCity, shipZip) "
        "VALUES (%s, CURDATE(), %s, %s, %s)"
    )
    cursor.execute(insert_order_query, (user_id, ship_address, ship_city, ship_zip))

    order_id = cursor.lastrowid

    for book in cart:
        insert_order_details_query = (
            "INSERT INTO book_store.odetails (ono, isbn, qty, amount) "
            "VALUES (%s, %s, %s, %s)"
        )
        values = (order_id, book["isbn"], book["qty"], book["qty"] * book["price"])
        cursor.execute(insert_order_details_query, values)

    connection.commit()

    cursor.close()
    connection.close()

    print(f"Order {order_id} created successfully!")
    return order_id


def clear_cart(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM book_store.cart WHERE book_store.cart.userid = %s", (user_id,)
    )
    connection.commit()
    cursor.close()
    connection.close()
