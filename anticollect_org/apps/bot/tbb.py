import os
import telebot
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt


mainPath = os.getcwd()
fileData = os.getcwd()+'/data.txt'
apikey = ''
bot = telebot.TeleBot(apikey, threaded=False)
link = ''



@csrf_exempt
def sbot(request):
    if request.META['CONTENT_TYPE'] == 'application/json':
        json_data = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])
        return HttpResponse("OK its work")
    else:
        return PermissionDenied



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    with open(fileData, 'r', encoding='UTF-8') as f:
        users = f.read().split('\n')
        thisUser = str(message.from_user.id)

        try:
            if(users.index(thisUser)>=0):
                print('dobavlen')
            bot.send_message(message.from_user.id, f'Ваш номер уже есть в базе')
        except:
            with open(fileData, 'a', encoding='UTF-8') as fr:
                # addUser = str(update_id) + '\n'
                addUser = str(message.from_user.id) + '\n'
                fr.write(addUser)
            bot.send_message(message.from_user.id, f'Я бот. Приятно познакомиться, {message.from_user.first_name} ваш номер. \nЯ буду сообщать о новых заказах на сайте')

def new_clients(text):
    filepath = mainPath + '/data.txt'
    with open(filepath, 'r', encoding='UTF-8') as f:
        usersRawArrey = f.read().split('\n')
        usersArrey = usersRawArrey[:-1]
        for i in usersArrey:
            bot.send_message(chat_id=i, text=text)
bot.remove_webhook()
bot.set_webhook(url=f"{link}/")
