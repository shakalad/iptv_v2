import sys

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from configs.bot_configs import token
from handlers.json_handler import JsonHandler
from handlers.pytest_handler import PytestHandler
from handlers.exception_handler import NotEnoughMoneyException


class BotHandler:
    def __init__(self):
        self.__bot = Bot(token=token)
        self.__dispatcher = Dispatcher(self.__bot)
        self.__json_handler = JsonHandler()
        self.__pytest_handler = PytestHandler()

    async def start(self, message: types.Message):
        await message.reply("I'm active now, and ready for your commands.")

    async def send_message(self, chat_id, text):
        await self.__bot.send_message(chat_id=chat_id, text=text)

    async def create_command(self, chat_id, email):
        await self.send_message(chat_id, "Starting new user registration")
        self.__json_handler.update_data('email', "ipservice2023+" + email + "@gmail.com")
        try:
            self.__pytest_handler.create_user()
        except NotEnoughMoneyException:
            await self.send_message(chat_id=chat_id, text=f'{str(NotEnoughMoneyException)}')
            return
        new_email = self.__json_handler.read_file()['email']
        await self.send_message(chat_id=chat_id, text=f'{new_email} was successfully created')

    async def recharge_command(self, chat_id, email, amount="1"):
        await self.send_message(chat_id, f"I start recharging the {email} in the amount of {amount}$")
        self.__json_handler.update_data('email', email)
        self.__json_handler.update_data('amount', amount)
        try:
            self.__pytest_handler.recharge_user()
        except NotEnoughMoneyException as e:
            await self.send_message(chat_id=chat_id, text=f'{str(e)}')
            return

    async def balance_command(self, chat_id):
        await self.send_message(chat_id, "Starting to check admin balance")
        self.__pytest_handler.check_balance()

    async def get_message(self, message: types.Message):
        chat_id = message.chat.id
        if "/create" in message.text:
            new_user_email = message.text.split(" ")[1]
            try:
                await self.create_command(chat_id=chat_id, email=new_user_email)
            except NotEnoughMoneyException as e:
                await self.send_message(chat_id=chat_id, text=f'{e}')
        elif "/recharge" in message.text:
            l_str = message.text.split(" ")
            user_email = l_str[1]
            if len(l_str) > 2:
                amount = l_str[2]
                await self.recharge_command(chat_id=chat_id, email=user_email, amount=amount)
            else:
                await self.recharge_command(chat_id=chat_id, email=user_email)
        elif "/balance" in message.text:
            await self.balance_command(chat_id)

        admin_balance = self.__json_handler.read_file()['admin_balance']
        await self.send_message(chat_id=chat_id, text=f'Admin Balance: {admin_balance}')

    def register_handlers(self):
        self.__dispatcher.register_message_handler(self.start, commands=['start'])
        self.__dispatcher.register_message_handler(self.get_message)

    def start_polling(self):
        executor.start_polling(self.__dispatcher, skip_updates=True)
