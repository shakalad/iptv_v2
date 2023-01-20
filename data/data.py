from dataclasses import dataclass


@dataclass()
class User:
    username: str = None
    email: str = None
    password: str = None
    repassword: str = None
