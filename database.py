import mysql.connector as sconnect


def get_connection():
    return sconnect.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root_password",
    )


if __name__ == "__main__":
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM book_store.books
        LIMIT 10
        """)
    data = cursor.fetchall()
    print(data)
