import telebot
from telebot.types import Message
import config
import random
bot = telebot.TeleBot(config.token)


hello = "\U0001f91a"
like = "\U0001f60a"
palm = "\U0001f334"
strawberry = "\U0001f353"
applodisments = '\U0001f44f'
kaktus = '\U0001f335'
love = '\U0001F496'

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Здравствуйте'+ hello +' Это официальный бот магазина электронной и бытовой техники "Electronik Center". Чтобы участвовать в конкурсе ОТПРАВЬТЕ ЛЮБОЕ ЧИСЛО ОТ 1 ДО 100 В БОТ (например, 16 или 92), а также убедитесь, что Вы подписаны на два телеграм канала')

@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    print(message.from_user.username,':',message.text)

    if message.chat.id != 447504115:
       chat_id = str(message.chat.id)
       bot.send_message(447504115, chat_id)
       if message.from_user.username == None:
        bot.send_message(447504115,'Мой Повелитель' +love+'Вам пришло сообщение!'  + like + '\n' +  chat_id+ ': ' + message.text + 
        '\n' 'Чтобы ответить - введите "Номер id: cообщение"', )
       elif message.from_user.username != None:
        bot.send_message(447504115,'Мой Повелитель' +love+'Вам пришло сообщение!'  + like + '\n' + '' + message.from_user.username + ' ('+  chat_id+ '): ' + message.text + 
        '\n' 'Чтобы ответить - введите "Номер id: cообщение"', )
        
       bot.send_message(message.chat.id,'Ваше сообщение отправлено! Ожидайте результатов конкурса. Наша компания продолжит сотрудничество с телеграм каналами, поэтому если Вам не повезет в этот раз, мы уверены, повезет в следующем конкурсе ' + like)
       
    else:
        answer = message.text
        response=''
        chat_id=''
        i=0
        if len(answer)>9:
           if answer[9]==':' :
            while answer[i]!=':':
               chat_id=chat_id+answer[i]
               i=i+1
            print(chat_id)
            i=i+1
            while i<len(answer):
               response=response+answer[i]
               i=i+1
            print(response)
            bot.send_message(chat_id,'Вам пришло сообщение! ')
            bot.send_message(chat_id,'*Сообщение от Эмиля: *'+ response, parse_mode= 'Markdown')
   


bot.polling()