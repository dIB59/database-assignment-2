import database
import user_input


def login():
    print("login user")


def register():
    connection = database.get_connection()
    user_data = user_input.collect_user_data()
    database.register_user(
        user_data[0],
        user_data[1],
        user_data[2],
        user_data[3],
        user_data[4],
        user_data[5],
        user_data[5],
        user_data[6],
        connection
    )
    return
