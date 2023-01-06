import re
from typing import Dict
from collections import defaultdict


def validate_types(form: Dict):
    """Creates new dict with validated types of original dict under same key names"""
    form_types = defaultdict(str)

    for key, value in form.items():
        form_types[key] = check_types(value)

    return form_types


def check_types(value):
    """Validates input value against date, phone, email patterns.
    If none matches, value counts as 'text' """
    if re.match(r"^(([0-2][0-9]|30|31)\.(0[1-9]|1[0-2])\.([0-2]\d{3}))|^(([0-2]\d{3})-(0[0-9]|1[0-2])-([0-2][0-9]|30|31))", value):
        return 'date'
    elif re.match(r"^(\+7 \d{3} \d{3} \d{2} \d{2})", value):
        return 'phone'
    elif re.match(r"^(\w+@\w+.\w+)", value):
        return 'email'
    else:
        return 'text'
