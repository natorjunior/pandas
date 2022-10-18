import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import random
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
msgs = [
    'Olá',
    'Como vai?',
    'Olá',
    'de boa ',
    'hi',
]
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, eu sou o BOT, como vai?")
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #Exemplo para enviar uma imagem
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('test.png', 'rb'))
    #Exemplo para enviar uma mensagem
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msgs[random.randint(0,len(msgs)-1)])

if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    
    application.run_polling()