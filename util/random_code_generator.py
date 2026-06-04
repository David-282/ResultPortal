import random


def matric_code():

    random_number = random.randint(100000, 999999)

    return f"RSP+{random_number}"