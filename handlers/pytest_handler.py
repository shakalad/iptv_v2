import subprocess

from configs.pytest_configs import *
from handlers.exception_handler import NotEnoughMoneyException


class PytestHandler:
    def __init__(self):
        self.___create_command = create
        self.___recharge_command = recharge
        self.___check_command = check

    def __execute(self, command):
        if subprocess.call(command, shell=True, stderr=subprocess.PIPE) != 0:
            raise NotEnoughMoneyException

    def create_user(self):
        self.__execute(self.___create_command)

    def recharge_user(self):
        self.__execute(self.___recharge_command)

    def check_balance(self):
        self.__execute(self.___check_command)
