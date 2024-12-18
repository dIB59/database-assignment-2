import mysql.connector as sconnect
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection


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


if __name__ == "__main__":
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM book_store.books
        LIMIT 10
        """
    )

    data = cursor.fetchall()
    print(data)

    connection = get_connection()
    register_user(
        fname="John",
        lname="Doe",
        address="123 Main St",
        city="New York",
        zip=10001,
        phone="1234567890",
        email="john.doe@example.com",
        password="hashed_password",
        connection=connection,
    )
    cursor.close()
