from telegram.ext import *
from bot.credentials import bot_token,bot_user_name,URL
import Responses as R
from jinja2.nodes import Filter

# https://api.telegram.org/bot1634245799:AAEbsSfzXlzbfS7IuVY1t_KCxvoczwyvknk/getme

print("Bot Started")
def start_command(update,context):
    update.message.reply_text("Type something ")
def handle_message(update,context):
  text= str(update.message.text).lower()
  response = R.sample_response(text)
  update.message.reply_text(response)
# def downloader(update, context):
#     context.bot.get_file(update.message.document).download()
#     with open("Handwrittentext/images/file.doc", 'wb') as f:
#         context.bot.get_file(update.message.document).download(out=f)

# def image_handler(update,context):
#     file = context.bot.getFile(update.message.photo[-1].file_id)
#     print ("file_id: " + str(update.message.photo[-1].file_id))
#     file.download('Handwrittentext/images/image.jpg')
#     print(str(hd.trainer())) 
           
def error(update,context):
  print(f"Update {update} caused error {context.error}")  
def main():
    updater = Updater(bot_token,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    # dp.add_handler(MessageHandler(Filter.document,downloader))
    # dp.add_handler(MessageHandler(Filters.photo, image_handler))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
main()