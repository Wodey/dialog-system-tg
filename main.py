import telebot
import requests

bot = telebot.TeleBot('6152404098:AAH85PecY07v8hM_Ka46__3-fMGtf12LjmI')
server_uri = "http://127.0.0.1:8000/"

@bot.message_handler(commands=['start'])
def hello(message):
    chat_id = message.chat.id 
    bot.send_message(chat_id, 'Напиши мне что-нибудь')
    
@bot.message_handler(commands=['clear'])
def clear(message):
    chat_id = message.chat.id 
    r = requests.delete(server_uri + f'clear_memory/{str(chat_id)}')
    if r.status_code == 200:
        bot.send_message(chat_id, 'Успех')
    else:
        bot.send_message(chat_id,f'Ошибка {r.status_code}')

@bot.message_handler(func=lambda message: True)
def answer_user(message):
    chat_id = message.chat.id 
    text = message.text 
    r = requests.post(server_uri + "get_model_response", json={
        "prompt": text, 
        "username": str(chat_id)
    })
    bot.send_message(chat_id, r.text)

bot.polling()