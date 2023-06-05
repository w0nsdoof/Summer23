from telebot import types , telebot
from datetime import datetime
from info import weekday, week_numero, semester
from telegram import InlineQueryResultArticle, InputTextMessageContent
from weather import openweather , get_weather_emoji
import requests, json

bot_api = "<Hide>" #Hide
bot = telebot.TeleBot(bot_api)

# In bot

"""
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

"""        

@bot.message_handler(commands=['weather'])
def info_weather(message):
    city = message.text.split('/weather')[1].strip()

    data = openweather(city)

    if isinstance(data, dict) :
        emoji = get_weather_emoji(data['Weather_report'])

        text = f"""Current weather in {data['City'].capitalize()}:
{emoji}{data['Weather_report'].capitalize()}
💨Wind speed: {data['Speed']} m/s
🌡Temperature: {data['Temperature']}°C
        """

    else:
        text = f"Wrong city: {city}"

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['university', 'kbtu', 'semester' , 'sem'])
def info_university(message):
    sem = semester()[0]
    cnt_w = week_numero()
    day = weekday()
    
    text = f"""{sem} semester
🕙Current week: {cnt_w}
🗓Day of week: {day} 
    """

    # text = f"{temp:-^40}\n" + f"Semester: {sem}\n" + f"Current week: {week_n}\n" + f"Day of the week: {week_d}"
    
    bot.send_message(message.chat.id, text)

# In chat

@bot.inline_handler(lambda query: len(query.query) == 0)
def inline_handler(inline_query):
    if True: # Output text
        data = openweather('Almaty')

        emoji = get_weather_emoji(data['Weather_report'])

        weather_text = f"""Current weather in {data['City'].capitalize()}:
{emoji}{data['Weather_report'].capitalize()}
💨Wind speed: {data['Speed']} m/s
🌡Temperature: {data['Temperature']}°C
        """

        sem = semester()[0]
        cnt_w = week_numero()
        day = weekday()
    
        university_text = f"""{sem} semester
🕙Current week: {cnt_w}
🗓Day of week: {day} 
    """  

    try:
        r1 = types.InlineQueryResultArticle('1', 'Weather', types.InputTextMessageContent(weather_text))
        r2 = types.InlineQueryResultArticle('2', 'University', types.InputTextMessageContent(university_text))
        bot.answer_inline_query(inline_query.id, [r1, r2])
    except Exception as e:
        print(e)


bot.polling(none_stop=True, interval=0)