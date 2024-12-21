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


class UserBuilder:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.address = ""
        self.city = ""
        self.zip = ""
        self.phone = ""
        self.email = ""
        self.password = ""

    def set_fname(self, fname: str):
        self.fname = fname
        return self

    def set_lname(self, lname: str):
        self.lname = lname
        return self

    def set_address(self, address: str):
        self.address = address
        return self

    def set_city(self, city: str):
        self.city = city
        return self

    def set_zip(self, zip: str):
        self.zip = zip
        return self

    def set_phone(self, phone: str):
        self.phone = phone
        return self

    def set_email(self, email: str):
        self.email = email
        return self

    def set_password(self, password: str):
        self.password = password
        return self

    def build(self):
        return User(
            self.fname,
            self.lname,
            self.address,
            self.city,
            self.zip,
            self.phone,
            self.email,
            self.password,
        )
