from data.data import User
from faker import Faker


def get_random_username(words=2):
    random_word = []
    for i in range(0, words):
        random_word.append(faker.word())
    return "".join(random_word)


faker = Faker()
Faker.seed()
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
        username=get_random_username(),
        email=get_last_email(),
        password=password,
        repassword=password,
    )
