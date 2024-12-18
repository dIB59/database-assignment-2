from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

import database


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
    insert_query = ("INSERT INTO book_store.members (fname, lname, address, city, zip, phone, email, password) VALUES "
                    "(%s, %s, %s, %s, %s, %s, %s, %s)")
    values = (fname, lname, address, city, zip, phone, email, password)
    cursor.execute(insert_query, values)
    connection.commit()
    connection.close()


if __name__ == "__main__":
    connection = database.get_connection()
    register_user(
        fname="John",
        lname="Doe",
        address="123 Main St",
        city="New York",
        zip=10001,
        phone="1234567890",
        email="john.doe@example.com",
        password="hashed_password",
        connection=connection
    )