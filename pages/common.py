from enum import Enum


class Emails(str, Enum):
    EMAIL = 'test@gmail.com'
    WRONG_EMAIL = 'sdfaadfa'


class Passwords(str, Enum):
    PASSWORD = 'test@gmail.com'
    WRONG_PASSWORD = 'sdfsfsfsdf'


class Exceptions(Exception):
    pass