import json , requests

api_key = "" # Hide 

def get_weather_emoji(weather_report):
    emoji_dict = {
        'clear sky': '☀️',
        'few clouds': '🌤️',
        'scattered clouds': '⛅️',
        'broken clouds': '☁️',
        'overcast clouds': '☁️',
        'light rain': '🌧️',
        'moderate rain': '🌧️',
        'heavy rain': '🌧️',
        'drizzle': '🌦️',
        'thunderstorm': '⛈️',
        'snow': '❄️',
        'mist': '🌫️',
        'fog': '🌫️',
        'haze': '🌫️',
        'smoke': '🌫️',
        'dust': '🌫️',
        'sand': '🌫️',
        'ash': '🌫️',
        'squalls': '💨'
    }

    emoji = emoji_dict.get(weather_report, "")

    return emoji


def openweather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric" + "&lang=eng"

    response = requests.get(url)

    if response.status_code == 200: 
        data = response.json()

        main = data['main']

        city = data['name']
        temperature = main['temp']
        speed = data["wind"]["speed"]
        weather_report = data['weather'][0]['description']

        result = {
            "City" : city ,
            "Temperature" : temperature ,
            "Speed" : speed ,
            "Weather_report" : weather_report
        }
        return result
    else:
        return "Error in HTTP request"
