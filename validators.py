import re


def validate_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True

    return False


def validate_phone(phone: str) -> bool:
    phone = phone.replace(" ", "")
    phone = phone.replace("-", "")

    pattern = r"^\+7\d{10}$"
    if re.match(pattern, phone):
        return True

    return False


def validate_date(date: str) -> bool:
    pattern_dd_mm_yyyy = r'^\d{2}\.\d{2}\.\d{4}$'
    pattern_yyyy_mm_dd = r'^\d{4}-\d{2}-\d{2}$'

    if re.match(pattern_dd_mm_yyyy, date):
        return True

    if re.match(pattern_yyyy_mm_dd, date):
        return True

    return False
