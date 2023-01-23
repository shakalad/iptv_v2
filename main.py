from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


import subprocess


bot = Bot(token="5905955278:AAFZ6CnIAE8GBDm8x4lI8EHjUeIZLcNcJBE")
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    if message.text == "/create":
        await bot.send_message(chat_id=chat_id, text="Starting to create a new user")
        subprocess.call("bash_files/create.sh", shell=True)
        with open("temp_files/new_user.txt", "r") as file:
            user_data = file.readlines()
        with open("temp_files/admin_balance.txt", "r") as file:
            admin_balance = file.readline()
        await bot.send_message(chat_id=chat_id, text=f"{user_data[0].strip()}")
        await bot.send_message(chat_id=chat_id, text=f"{user_data[1]}")
        await bot.send_message(chat_id=chat_id, text=f"Admin Balance: {admin_balance}")
        await bot.send_message(chat_id=chat_id, text=f"User was successfully created")
    elif "/recharge" in message.text:
        username = message.text.split(" ")[1]
        with open("temp_files/email_user.txt", "w") as file:
            file.write(username)
        await bot.send_message(chat_id=chat_id, text=f"I start recharging the {username}'s account")
        subprocess.call("bash_files/recharge.sh", shell=True)
        with open("temp_files/admin_balance.txt", "r") as file:
            admin_balance = file.readline()
        await bot.send_message(chat_id=chat_id, text=f"User: {username} was topped up with 1$")
        await bot.send_message(chat_id=chat_id, text=f"Admin Balance: {admin_balance}")
    elif message.text == "/balance":
        await bot.send_message(chat_id=chat_id, text="Starting to check admin balance")
        subprocess.call("bash_files/check.sh", shell=True)
        with open("temp_files/admin_balance.txt", "r") as file:
            admin_balance = file.readline()
        await bot.send_message(chat_id=chat_id, text=f"On your account: {admin_balance}")

executor.start_polling(dp)

