import comands as com  # команды
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}! Системное время {com.dat()}')

async def msg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    text = update.message.text

    comands = {
        '*время*': com.dat(),
        'cm': 10 ** -2,
        'dm': 10 ** -1,
    }

    if text in comands:
        text = comands[text]
    else:
        text = 'Команда не распознана'

    print(f'{str(text)}')

    await update.message.reply_text(f'{str(text)}')

app = ApplicationBuilder().token("5841883746:AAHVa8mWrcs7n1NS3KlxP7UtacAvpfe_KWU").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT.strings, msg))

app.run_polling()