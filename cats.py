import requests
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup,KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

def echo(bot, update):
    update.message.reply_text("Undefined...")
    bot.forwardMessage(chat_id=350279190,from_chat_id=update.message.chat_id,message_id=update.message.message_id)

def start(bot, update):
    update.message.reply_text("Hello! Do U wanna get some cats  (¬_¬ )\nType /cat and U will get 'em...")

def helping(bot, update):
    update.message.reply_text('Only one command, dude, /cat...\nhmm, stop, actually two, nevermind...\nNOW THERE ARE SEVERAL  w(ﾟｏﾟ)w')

def getcat():
    try:
        r=requests.get('https://api.thecatapi.com/api/images/get?format=src')
        url = r.url
    except:
        url=get_cat()
    return url

def sendcat(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.UPLOAD_PHOTO)
    bot.sendPhoto(chat_id=update.message.chat_id, photo=getcat(),reply_markup=draw_button())

def ready(bot, update):
    update.message.reply_text("Ready...")
    #bot.sendMessage(chat_id=update.message.chat_id, text='ready', parse_mode=Markdown)

def test(bot, update):
    bot.send_message(chat_id=update.message.chat_id,text='*GOT IT!*', parse_mode=telegram.ParseMode.MARKDOWN)
    #bot.send_photo(chat_id=update.message.chat_id, photo=open('C:\\Users\\Tigran_K\\Desktop\\python 3\\bots\\third__\\image.jpg', 'rb'))

def draw_button():
    keys=[[InlineKeyboardButton('Something more?  (¬‿¬ )', callback_data='1'), InlineKeyboardButton('NO NO NO', callback_data='2')]]
    return InlineKeyboardMarkup(inline_keyboard=keys)

def get_callback_from_button(bot, update):
    query = update.callback_query
    username = update.effective_user.username
    chat_id = query.message.chat.id
    message_id = query.message.message_id
    if int(query.data) == 1:
        bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.UPLOAD_PHOTO)
        bot.sendPhoto(photo=getcat(), chat_id=chat_id, message_id=message_id, reply_markup=draw_button())
    elif int(query.data)==2:
        bot.sendMessage(chat_id=chat_id,text='OK OK OK, dude, calm down  (o_O)')

def sendgif(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.UPLOAD_DOCUMENT)
    bot.sendAnimation(chat_id=update.message.chat_id, file_id='CgADBAADewAD30u8Un0kwRZ94J0wAg')

def main():
    updater = Updater("721020886:AAEFdaOC6LZcM9T2x-D5QpBl6MEvAwLZ8LU")
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('gif', sendgif))
    dp.add_handler(CommandHandler('help', helping))
    dp.add_handler(CommandHandler('cat', sendcat))
    dp.add_handler(CommandHandler('ready', ready))
    dp.add_handler(CommandHandler('test', test))
    dp.add_handler(CallbackQueryHandler(get_callback_from_button))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
