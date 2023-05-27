from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from configs.bot_configs import token
from handlers.json_handler import JsonHandler
from handlers.pytest_handler import PytestHandler


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
        self.__json_handler.update_data('email', email)
        self.__pytest_handler.create_user()

    async def recharge_command(self, chat_id, email, amount="1"):
        await self.send_message(chat_id, f"I transfer money to the {email} in the amount of {amount}$")
        self.__json_handler.update_data('email', email)
        self.__pytest_handler.recharge_user()

    async def balance_command(self, chat_id):
        await self.send_message(chat_id, "Want to know how much money is left in your account? Let me help you")
        self.__pytest_handler.check_balance()

    async def get_message(self, message: types.Message):
        chat_id = message.chat.id
        if "/create" in message.text:
            new_user_email = message.text.split(" ")[1]
            await self.create_command(chat_id=chat_id, email=new_user_email)
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

    def register_handlers(self):
        self.__dispatcher.register_message_handler(self.start, commands=['/start'])
        self.__dispatcher.register_message_handler(self.get_message)

    def start_polling(self):
        executor.start_polling(self.__dispatcher, skip_updates=True)
