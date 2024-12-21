from typing import NamedTuple


class NewUser(NamedTuple):
    fname: str
    lname: str
    address: str
    city: str
    zip: str
    phone: str
    email: str
    password: str


class User(NamedTuple):
    fname: str
    lname: str
    address: str
    city: str
    zip: str
    phone: str
    email: str
    user_id: int
    password: str
