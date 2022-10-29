import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import random
import requests
import pandas as pd
import json
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, eu sou o BOT, como vai?")


async def get_servidor_aleatorio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=pd.DataFrame(requests.get('http://127.0.0.1:8000/retorna_servidor_aleatorio').json()).iloc[0].to_markdown(index=False, tablefmt='pipe'),
        parse_mode = "Markdown"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    dados = {"nome": update.message.text}
    r = requests.get(
        "http://127.0.0.1:8000/retorna_servidor/",
        data = json.dumps(dados),
            headers={
            "Content-Type": "application/json"
        }
    )
    msg = pd.DataFrame(r.json())
    if len(msg)>0:
        msg = msg.iloc[0].to_markdown(index=False, tablefmt='pipe')
    else:
        msg = "Servidor nao encontrado "
    #Exemplo para enviar uma mensagem
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()
    start_handler = CommandHandler('start', start)
    start_servidor_aleatorio = CommandHandler('aleatorio', get_servidor_aleatorio)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(start_servidor_aleatorio)

    
    application.run_polling()
