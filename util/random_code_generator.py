import random


def matric_code(name):
    prefix = name[:3].upper()

    random_number = random.randint(100000, 999999)

    return f"{prefix}-{random_number}"