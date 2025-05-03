import re

EMAIL_PATTERN = r'^[a-z]+\.[a-z]+@university\.com$'
PASSWORD_PATTERN = r'^[A-Z][a-zA-Z]{5,}\d{3,}$'

def validate_email(email):
    return bool(re.match(EMAIL_PATTERN, email))

def validate_password(password):
    return bool(re.match(PASSWORD_PATTERN, password))