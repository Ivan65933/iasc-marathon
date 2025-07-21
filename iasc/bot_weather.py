import telebot
import requests

API_KEY = '51f923b44110fbf0283573dfaac5e87e' 
bot = telebot.TeleBot("7589630038:AAH4BNSneGv6mmNXS0UVbF1PNYi3JlQv7xA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Напиши назву міста, і я скажу тобі погоду 🌤")

@bot.message_handler(func=lambda message: True)
def get_weather(message):
    city = message.text
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ua"
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            bot.reply_to(message, f"Не знайшов погоду для '{city}' 😢")
        else:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            bot.reply_to(message, f"🌡 Температура у {city}: {temp}°C\n🌥 {description.capitalize()}")
    except Exception as e:
        bot.reply_to(message, "⚠️ Сталася помилка. Спробуй пізніше.")

bot.infinity_polling()