from data.data import User
from faker import Faker

import random
import string


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


faker = Faker()
Faker.seed()
random_username = get_random_string(16)
password = faker.password(special_chars=False).lower()


def get_last_email():
    with open("data/emails.txt", "r") as file:
        _list = file.read().strip()
        last_email = _list.split("\n").pop()
        print("\n")
        print("*"*20)
        print(f"{len(_list.split()) - 1} emails left")
        print("*"*20)

    with open("data/emails.txt", "w") as file:
        new_list = _list.replace(last_email, "")
        file.write(new_list)

    return last_email


def generated_user():
    yield User(
        username="".join(random_username.split()).lower(),
        email=get_last_email(),
        password=password,
        repassword=password,
    )
