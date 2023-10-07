from data.data import User
from faker import Faker
from handlers.json_handler import JsonHandler


def get_random_username(words=2):
    random_word = []
    for i in range(0, words):
        random_word.append(faker.word())
    return "".join(random_word)


faker = Faker()
Faker.seed()
password = "904070"


def generated_user():
    yield User(
        username=get_random_username(),
        email=JsonHandler().read_file()['email'],
        password=password,
        repassword=password,
    )
