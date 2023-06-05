from handlers.json_handler import JsonHandler
from configs.admin_config import admin_email, admin_password


class DataHandler:
    def __init__(self):
        self.__json_handler = JsonHandler()
        self.__admin_email = admin_email
        self.__admin_password = admin_password

    @property
    def user_email(self):
        return self.__json_handler.get(key="email")

    @property
    def admin_email(self):
        return self.__admin_email

    @property
    def user_password(self):
        return self.__json_handler.get(key="password")

    @property
    def admin_password(self):
        return self.__admin_password

    @property
    def admin_balance(self):
        return self.__json_handler.get("admin_balance")

    @property
    def amount(self):
        return self.__json_handler.get("amount")
