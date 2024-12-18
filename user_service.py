import database
import user_input
from user import User


def login():
    print("login user")
    connection = database.get_connection()
    email, password = user_input.get_login_data()
    user = database.login_user(
        email,
        password,
        connection
    )
    if user is None:
        print("User not found, please check if email or username is correct")
        return False
    return True


def register() -> User:
    connection = database.get_connection()
    user_data = user_input.collect_user_register_data()
    return database.register_user(
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
