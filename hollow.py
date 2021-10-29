import telebot
import os
import pickle
import datetime
path = os.getcwd()
print(path)
with open("users.dat", "rb") as f :
    apple = pickle.load(f)
passwords = apple[0]
messages = apple[1]
bot = telebot.TeleBot('1836330544:AAG-b8FJi90cPQ0eOXRKv3c7juaQw-HSvNE')
print(len(passwords))
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(messages)
    login = message.from_user.username
    passwords.add(message.from_user.username)
    offset = datetime.timezone(datetime.timedelta(hours=3))
    if message.from_user.username not in messages.keys():
        messages[message.from_user.username] = []
    if message.text == "/start":
        bot.send_message(message.from_user.id, 'Привет! Это Hollow Мессенджер! Напишите: /write имя_пользователя сообщение чтобы написать сообщение, /my_username чтобы узнать свой адрес для отправления сообщений и /look для прочитывания сообщений.')
    elif "/write" in message.text :
        while True :
            try :
                if message.text.split()[1] in passwords :
                    print("hello")
                    msg = ' '.join(message.text.split()[2:])
                    imac = str(datetime.datetime.now(offset))[:16]
                    messages[message.text.split()[1]].append([login, msg, imac])

                    bot.send_message(message.from_user.id, 'Сообщение отправлено!')
                    with open("users.dat", "wb") as qw :
                        pickle.dump([passwords, messages], qw)
                    break
                else :
                    bot.send_message(message.from_user.id, 'Этого пользователя не существует!')
                    break
            except :
                bot.send_message(message.from_user.id, 'Используйте синтаксис! /write имя_пользователя сообщение')
                break
    elif message.text == "/look" :
        print(len(messages[login]))
        for i in list(messages.items()) :
            if i[0] == login :
                if len(messages[login]) == 0 :
                    bot.send_message(message.from_user.id, "Нет непрочитанных сообщений!")
                for j in i[1] :
                    if len(messages[login]) == 0 :
                        bot.send_message(message.from_user.id, "Нет непрочитанных сообщений")
                    bot.send_message(message.from_user.id, f'''{j[0]} написал: {j[1]}
                    Дата и время отправки: {j[2]}''')
        messages[login] = []
    elif message.text == "/my_username" :
        bot.send_message(message.from_user.id, message.from_user.username)
    else :
        bot.send_message(message.from_user.id, "Я не понял, такой команды нет. Напишите /start")

bot.polling(none_stop=True, interval=1)