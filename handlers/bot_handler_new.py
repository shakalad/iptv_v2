import telebot
from telebot import types

from configs.bot_configs import token
from handlers.json_handler import JsonHandler
from handlers.pytest_handler import PytestHandler
from handlers.exception_handler import NotEnoughMoneyException


class BotHandler:
    def __init__(self):
        self.bot = telebot.TeleBot(token)
        self.json_handler = JsonHandler()
        self.pytest_handler = PytestHandler()

    def start_polling(self):
        self.bot.infinity_polling()

    def helper(self, message):
        self.bot.send_message(message.chat.id, "<b>Help <em>information!</em></b>", parse_mode="html")

    def main(self, message):
        print("Обработчик сработал: пользователь ввел 9-значное число")  # Логирование
        markup = types.InlineKeyboardMarkup()
        create_button = types.InlineKeyboardButton("🆕 ახალი მომხმარებლის რეგისტრაცია", callback_data="create_user")
        recharge_user = types.InlineKeyboardButton("💳 მომხმარებლის ბალანსის შევსება", callback_data="recharge_user")
        get_user_playlist_link = types.InlineKeyboardButton("🔗 მომხმარებლის ფლეილისთის ბმულის მიღება",
                                                            callback_data="get_user_playlist_link")
        activate_user = types.InlineKeyboardButton("✅ მომხმარებლის აქტივაცია", callback_data="activate_user")

        markup.row(create_button)
        markup.row(recharge_user)
        markup.row(get_user_playlist_link)
        markup.row(activate_user)
        self.bot.send_message(message.chat.id, f"რა ოპერაციის ჩატარება გსურთ ამ მომხმარებელზე {message.text} ?",
                              reply_markup=markup)

    def handle_wrong_length(self, message):
        num_digits = len(message.text)
        if num_digits < 9:
            self.bot.send_message(message.chat.id,
                                  "მითითებულია 9 ციფრზე ნაკლები, გთხოვთ მიუთოთ 9 ციფრიანი მნიშვნელობა ველში,"
                                  " ტელეფონის ნომერი უნდა გამოიყურებოდეს შემდეგნაირად 5xxxxxxxx")
        elif num_digits > 9:
            self.bot.send_message(message.chat.id,
                                  "მითითებულია 9 ციფრზე ნაკლები, გთხოვთ მიუთოთ 9 ციფრზე მეტი მნიშვნელობა ველში,"
                                  " ტელეფონის ნომერი უნდა გამოიყურებოდეს შემდეგნაირად 5xxxxxxxx")

    def handle_non_digit(self, message):
        self.bot.send_message(message.chat.id,
                              "ვერ გავიგე დავალება :( შეიყვანეთ ბრძანება /help რომ ნახოთ დავალებების ჩამონათვალი")

    def callback_query(self, call):
        original_message_text: str = call.message.text
        try:
            if call.data == "create_user":
                self.bot.answer_callback_query(call.id, "რეგისტრაციის პროცესი დაწყებულია."
                                                        " დასრულების შემდეგ მიიღებთ დამადასტურებელ შეტყობინებას.",
                                               show_alert=True)
                # Update json file
                self.json_handler.update_data('email', "ipservice2023+" + original_message_text + "@gmail.com")

                # Execute pytest command
                self.pytest_handler.create_user()

                # Read from json
                new_email = self.json_handler.read_file()['email']
                self.bot.send_message(call.message.chat.id, "<p>რეგისტრაციის პროცესი დასრულებულია.<p>"
                                                            f"<p>მომხმარებელი: {new_email}</p>", parse_mode="html")

            elif call.data == "recharge_user":
                self.bot.answer_callback_query(call.id, "მიმდინარეობს მომხმარებლის ბალანსის შევსება. გთხოვთ დაიცადოთ.",
                                               show_alert=True)

                # Update json file
                self.json_handler.update_data('email', original_message_text)
                # TODO implement amount of the recharge
                # self.json_handler.update_data('amount', amount)

                # Execute pytest command
                self.pytest_handler.recharge_user()

                self.bot.send_message(call.message.chat.id, "", parse_mode="html")

            elif call.data == "get_user_playlist_link":
                self.bot.answer_callback_query(call.id, "მიმდინარეობს მოთხოვნილი ფლეილისთის ბმულის მიღება. გთხოვთ "
                                                        "დაიცადოთ.",
                                               show_alert=True)
                # Some code
                self.bot.send_message(call.message.chat.id, "", parse_mode="html")

            elif call.data == "activate_user":
                self.bot.answer_callback_query(call.id, "მომხმარებლის აქტივაციის პროცესი დაწყებულია. გთხოვთ დაიცადოთ.",
                                               show_alert=True)

                # Update json
                self.json_handler.update_data('email', original_message_text)
                self.bot.send_message(call.message.chat.id, "<p>მომხმარებლის აქტივაციის პროცესი დასრულებულია.</p>",
                                      parse_mode="html")

        except Exception as e:
            self.bot.send_message("477632626", f"Error : {e}")
