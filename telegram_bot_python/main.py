from telebot import types , telebot
from datetime import datetime
from info import weekday, week_numero, semester
from telegram import InlineQueryResultArticle, InputTextMessageContent
from weather import openweather , get_weather_emoji , openweather_by_city
import requests, json

bot_api = "" #Hide
bot = telebot.TeleBot(bot_api)

# In bot

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)

    button1 = types.KeyboardButton('Weather')
    button2 = types.KeyboardButton('University')

    markup.add(button1, button2)

    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

@bot.message_handler(func=lambda message:True)
def button_interact(message):
    if message.text == 'Weather':
        info_weather(message)
    elif message.text == 'University':
        info_university(message)

@bot.message_handler(commands=['weather'])
def info_weather_by_city(message):
    city = message.text.split('/weather')[1]

    data = openweather_by_city(city)

    if data == dict :
        emoji = get_weather_emoji(data['Weather_report'])

        text = f"""Current weather in {data['City']}:
{emoji}{data['Weather_report'].capitalize()}
💨Wind speed: {data['Speed']} m/s
🌡Temperature: {data['Temperature']}°C
        """

    else:
        text = "Wrong city"

    bot.send_message(message.chat.id, text)




#Functions
def info_weather(message):
    data = openweather()

    emoji = get_weather_emoji(data['Weather_report'])

    text = f"""Current weather in {data['City']}:
{emoji}{data['Weather_report'].capitalize()}
💨Wind speed: {data['Speed']} m/s
🌡Temperature: {data['Temperature']}°C
        """

    bot.send_message(message.chat.id, text)
    #

def info_university(message):
    temp = "KBTU"
    sem = semester()[0]
    week_n = week_numero()
    week_d = weekday()
    
    text2 = f"""{sem} semester
🕙Current week: {week_n}
🗓Day of week: {week_d} 
    """

    # text = f"{temp:-^40}\n" + f"Semester: {sem}\n" + f"Current week: {week_n}\n" + f"Day of the week: {week_d}"
    
    bot.send_message(message.chat.id, text2)

""" 
# INLINE FUNCTIONS (Вызываемые в чате), OLD FUNCTIONS NEED TO CHANGE
@bot.inline_handler(func=lambda query: query.query == "weather")
def info_weather2(query):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city = "Almaty,KZ"
    api_key = "" #Hide

    url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric" + "&lang=eng"

    response = requests.get(url)

    if response.status_code == 200: 
        data = response.json()

        main = data['main']

        temperature = main['temp']
        speed = data["wind"]["speed"]
        weather_report = data['weather']

        text = f"{city:-^40}"+ f"\nTemperature: {temperature}°C" + f"\nWind speed: {speed} m/s" + "\nWeather report:" + weather_report[0]['description']
    
    result = telebot.types.InlineQueryResultArticle(
            id='1',
            title='Weather in Almaty',
            input_message_content=telebot.types.InputTextMessageContent(message_text=text)
        )

        # Отправка результатов в ответ на inline-запрос
    bot.answer_inline_query(query.id, [result])

@bot.inline_handler(func=lambda query: query.query == "kbtu")
def info_university2(query):
    temp = "KBTU"
    sem = semester()[0]
    week_n = week_numero()
    week_d = weekday()
    
    text = f"{temp:-^40}\n" + f"Semester: {sem}\n" + f"Current week: {week_n}\n" + f"Day of the week: {week_d}"
    
    result = telebot.types.InlineQueryResultArticle(
            id='1',
            title='Info KBTU',
            input_message_content=telebot.types.InputTextMessageContent(message_text=text)
        )

        # Отправка результатов в ответ на inline-запрос
    bot.answer_inline_query(query.id, [result])
"""

bot.polling(none_stop=True, interval=0)