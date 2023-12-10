#Написать бота который будет проверять доступность сайта
import ping3
import telebot
from telebot import types
bot = telebot.TeleBot("")

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.from_user.id, "О привет! (возможно снова) Добро пожаловать в проверку доступности сайта")
    r = start()
    if r != "null":
        bot.send_message(message.from_user.id, r)
    else:
        showSites(message)
@bot.message_handler(commands=["addSite"])
def add_site(message):
    bot.send_message(message.from_user.id, "Добавляем сайт? Окей. . . ")
    bot.send_message(message.from_user.id, "Введите сайт для добавления в запомненные")
    bot.register_next_step_handler(message, addSite)

def start():
    with open("1.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
    le = len(lines)
    if le < 1:
        return "Добавьте сайт в запомненные, а затем выберите его для проверки статуса :)"
    else:
        return "null"



def addSite(message):
    with open("1.txt", "a") as f:
        f.write(message.text+"\n")
    bot.send_message(message.from_user.id, message.text + " успешно добавлен")

def showSites(message):
    print("showSites")
    markup = types.InlineKeyboardMarkup()
    with open("1.txt", "r", encoding="UTF-8") as f:
        for e in f:
            print(e)
            markup.add(types.InlineKeyboardButton(e, callback_data=e))
    bot.send_message(message.from_user.id, text="Уже существуют добавленные сайты, выберите один из них. . .", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def pinging(callback):
    bot.send_message(callback.message.chat.id, "Окей, начинаем проверку сайта " + callback.data)
    resp = ""
    for e in range(10):
        ip_address = callback.data.replace("\n","")
        result = ping3.ping(ip_address)
        if result != False:
            resp += f"Результат пингования {ip_address}: {result} мс \n"
        else:
            resp += f"Результат пингования - сервер {ip_address} недоступен \n"

    bot.send_message(callback.message.chat.id, resp)
    bot.send_message(callback.message.chat.id, "Попробуем снова? /start, добавим /addSite")


bot.polling(none_stop=True, interval=0)