# Alterando as funcionalidades do primeiro BOT Telegram 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


# Código para o primeiro BOT
```python
import logging
from telegram import Update
from telegram.ext import *
import random
logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	level=logging.INFO
)
msgs = ['Olá','Como vai?','Olá','de boa ','hi']
async  def  start(update, context):
	await context.bot.send_message(
		chat_id=update.effective_chat.id, 
		text="Olá, eu sou o BOT, como vai?"
	)
async  def  echo(update, context):
	#Exemplo para enviar uma mensagem
	await context.bot.send_message(
		chat_id=update.effective_chat.id,
		text=msgs[random.randint(0,len(msgs)-1)]
	)
if  __name__ == '__main__':
	application = ApplicationBuilder().token('TOKEN').build()
	start_handler = CommandHandler('start', start)
	echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
	application.add_handler(start_handler)
	application.add_handler(echo_handler)
	application.run_polling()
```
Execute o BOT no terminal
````terminal
python bot.py
````
