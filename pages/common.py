from enum import Enum
from faker import Faker

fake = Faker()


class Emails(str, Enum):
    EMAIL = 'test@gmail.com'
    EMAIL_FOR_REGISTRATION = fake.email()
    WRONG_EMAIL = ''


class Passwords(str, Enum):
    PASSWORD = 'test@gmail.com'
    WRONG_PASSWORD = ''


class Exceptions(Exception):
    pass
