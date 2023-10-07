from handlers.bot_handler import BotHandler

bot = BotHandler()
bot.register_handlers()
bot.start_polling()
