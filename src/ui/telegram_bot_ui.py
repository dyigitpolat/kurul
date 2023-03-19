from kurul.kurul import *

from telegram.ext import *
import telegram

class TelegramBotUI:
    def __init__(self, token, authorized_chat_ids):
        self.application = Application.builder().token(token).build()
        self.authorized_chats = authorized_chat_ids

        self.kurul_sessions = {}
        for chat_id in authorized_chat_ids:
            self.kurul_sessions[chat_id] = Kurul()

    async def __message_handler(self, update, context):
        message = update.message
        chat_id = message.chat_id
        text = message.text

        await context.bot.send_chat_action(chat_id=chat_id, action=telegram.constants.ChatAction.TYPING)

        if chat_id in self.authorized_chats:
            response = self.kurul_sessions[chat_id].respond(text)
            await context.bot.send_message(chat_id=chat_id, text=response)
        else:
            await context.bot.send_message(chat_id=chat_id, text=f"You are not authorized to use this bot. Chat id: {chat_id}")

    def start(self):
        self.application.add_handler(MessageHandler(filters.TEXT, self.__message_handler))
        self.application.run_polling(1.0)