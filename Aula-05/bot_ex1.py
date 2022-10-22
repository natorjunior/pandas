import logging
from telegram import Update
from telegram.ext import *
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
async def start(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Olá, eu sou o BOT, como vai?"
    )
app = ApplicationBuilder().token('5756002288:AAEiHJzE-Nvm7B7EjJHamhNF0hQCRVZ7_uE').build()
start_handler = CommandHandler('start', start)
app.add_handler(start_handler)
app.run_polling()