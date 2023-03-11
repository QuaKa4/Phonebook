from enum import Enum

from faker import Faker

fake = Faker()

class Emails(str, Enum):
    EMAIL = 'test@gmail.com'
    EMAIL_FOR_REGISTRATION = fake.email()
    WRONG_EMAIL = 'sdfaadfa'


class Passwords(str, Enum):
    PASSWORD = '88005553535'
    WRONG_PASSWORD = 'sdfsfsfsdf'


class Exceptions(Exception):
    pass
