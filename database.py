import mysql.connector as sconnect


def get_connection(url: str = "127.0.0.1"):
    return sconnect.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root_password",
    )


if __name__ == "__main__":
    connection = cxt = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM book_store.books
        LIMIT 10
        """)
    data = cursor.fetchall()
    print(data)
