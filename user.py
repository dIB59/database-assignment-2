from typing import NamedTuple


class User(NamedTuple):
    fname: str
    lname: str
    address: str
    city: str
    zip: str
    phone: str
    email: str
    password: str
