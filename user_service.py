import database
import user_input
from user import User


def login() -> User | None:
    print("login user")
    connection = database.get_connection()
    email, password = user_input.get_login_data()
    user = database.login_user(email, password, connection)
    return User(*user) if user else None


def register() -> User or None:
    connection = database.get_connection()
    user_data = user_input.collect_user_register_data()
    return database.register_user(
        user_data.fname,
        user_data.lname,
        user_data.address,
        user_data.city,
        user_data.zip,
        user_data.phone,
        user_data.email,
        user_data.password,
        connection
    )
