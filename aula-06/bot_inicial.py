import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import random
import requests
import pandas as pd
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, eu sou o BOT, como vai?")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    msg = 'recebemos sua mensagem: '+update.message.text
    #Exemplo para enviar uma mensagem
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    
    application.run_polling()
