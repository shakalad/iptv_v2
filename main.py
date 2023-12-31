from handlers.bot_handler_new import BotHandler

handler = BotHandler()


handler.bot.message_handler(commands=['help'])(handler.helper)
handler.bot.message_handler(func=lambda message: message.text.isdigit() and len(message.text) == 9)(handler.main)
handler.bot.message_handler(func=lambda message: message.text.isdigit())(handler.handle_wrong_length)
handler.bot.message_handler(func=lambda message: not message.text.isdigit())(handler.handle_non_digit)
handler.bot.callback_query_handler(func=lambda call: True)(handler.callback_query)


handler.start_polling()
