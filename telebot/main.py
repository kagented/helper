import datetime as dt
import cred, reply, task
from telegram.ext import *

print('Bot started')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = reply.sample(text)
    update.message.reply_text(response)

def start_command(update, context):
    update.message.reply_text('Type something')

def help_command(update, context):
    update.message.reply_text('Google!')

def send_sheet(update, context):
    print(update)
    chat_id = update.message.chat_id
    filepath = r'C:\\GitHub\\worship_assistant\\data\\sheet\\'
    # imgname = '성도여다함께.jpg'
    filename = update["message"]["text"].split()[1]+'.jpg'
    sheet = open(filepath+filename, 'rb')
    context.bot.send_document(chat_id,sheet)

def send_ppt(update, context):
    print(update)
    chat_id = update.message.chat_id
    filepath = r'C:\\GitHub\\worship_assistant\\data\\ppt\\'
    # imgname = '성도여다함께.jpg'
    filename = update["message"]["text"].split()[1]+'.ppt'
    sheet = open(filepath+filename, 'rb')
    context.bot.send_document(chat_id,sheet)

def prayer_command(update, context):
    update.message.reply_text('오늘의 나라사랑정오기도 \n'+dt.datetime.now().strftime("%Y-%m-%d"))
    update.message.reply_text(task.show_prayer())

def error(update, context):
    # print(update)
    print(context.error)


def main():
    updater = Updater(cred.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("sheet", send_sheet))
    dp.add_handler(CommandHandler("prayer", prayer_command))
    dp.add_handler(CommandHandler("ppt", send_ppt))
    # dp.add_handler(CommandHandler("말씀", send_sheet))



    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()

