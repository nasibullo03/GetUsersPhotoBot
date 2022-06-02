from pyparsing import empty
import telebot
from telebot import types
from config import TOKEN_Telegram
import time
import logging
import sys
from pprint import *
from vk_parsing import getUserPhotos

bot = telebot.TeleBot(TOKEN_Telegram)

def ButtonsOnStart():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Показать фотографии')
    return markup

def GetPhotoArray(photos):
    arrayPhotoTypes = [] 
    for photo in photos:
        arrayPhotoTypes.append(telebot.types.InputMediaPhoto(photo))
    return arrayPhotoTypes
    # if len(arrayPhotoTypes)!= 0:
    #     bot.send_media_group(chatId,arrayPhotoTypes)
    #     arrayPhotoTypes = []
# Главное меню

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Здраствуйте {0.first_name}, Выберите команду".format(
        message.from_user), reply_markup=ButtonsOnStart())
  

@bot.message_handler(content_types=['text'])
def bot_message(message):

    textFromUser = message.text
    chatId = message.chat.id

    if message.text == 'Показать фотографии':
        bot.send_message(message.chat.id, "Пришлите мне ссылку на страничку vk")
    else:
        if 'vk.com' in message.text:
            link = message.text.split('/')[-1]
            imageUlrs = getUserPhotos(link)
            if imageUlrs != []:
                arrayPhotoTypes = [] 
                for photo in imageUlrs:
                    arrayPhotoTypes.append(telebot.types.InputMediaPhoto(photo))
                    if len(arrayPhotoTypes)==10:
                       bot.send_media_group(chatId,arrayPhotoTypes)
                       arrayPhotoTypes.clear()
                if len(arrayPhotoTypes)!=0:
                    bot.send_media_group(chatId,arrayPhotoTypes)
                    arrayPhotoTypes.clear()
            elif imageUlrs == []:
                    bot.send_message(chatId, 'Либо у данного пользователь закрытий профил, либо такого пользователь не существует!')
        else:
            bot.send_message(chatId,'Введите правильный url!')
                
# while True:
    
#     try:
#       bot.polling(none_stop=True)
#       pprint('Бот запущен')
#     except: 
#       print('Ощибка!!! бот остановилась')
#       logging.error('error: {}'.format(sys.exc_info()[0]))
#       time.sleep(5)


bot.polling(none_stop=True)

 