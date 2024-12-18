import mysql.connector as sconnect
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from user_service import User


def get_connection():
    return sconnect.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root_password",
    )


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
):
    cursor = connection.cursor()
    insert_query = (
        "INSERT INTO book_store.members (fname, lname, address, city, zip, phone, email, password) VALUES "
        "(%s, %s, %s, %s, %s, %s, %s, %s)"
    )
    values = (fname, lname, address, city, zip, phone, email, password)
    cursor.execute(insert_query, values)
    connection.commit()

    user_id = cursor.lastrowid

    select_query = "SELECT * FROM book_store.members WHERE book_store.members.userid = %s"
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
    select_query = "SELECT * FROM book_store.members WHERE book_store.members.email = %s AND password = %s"
    cursor.execute(select_query, (email, password))
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    return user


if __name__ == "__main__":
    connection = get_connection()
    user = register_user(
        fname="John2",
        lname="Doe2",
        address="123 Main St",
        city="New York",
        zip=10001,
        phone="1234567890",
        email="john.doe3@example.com",
        password="hashed_password",
        connection=connection,
    )
    connection.close()
    print(user)
