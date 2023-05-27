import subprocess

from configs.pytest_configs import *


class PytestHandler:
    def __init__(self):
        self.___create_command = create
        self.___recharge_command = recharge
        self.___check_command = check

    def __execute(self, command):
        subprocess.call(command, shell=True)

    def create_user(self):
        self.__execute(self.___create_command)

    def recharge_user(self):
        self.__execute(self.___recharge_command)

    def check_balance(self):
        self.__execute(self.___check_command)
