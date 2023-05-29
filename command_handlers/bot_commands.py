from .bot_functions import listen, say
import random
import webbrowser
import requests

from .commands import commands

OPEN_WEATHER_API_KEY = "8d24c9e287fbcb3e0ff18319bd2248bb"

def chooseComand(command):
    for key, value in commands.items():
        for i in value:
            if i in command:
                globals()[key]()


def startListen():
    text = listen()
    chooseComand(text)


def ok_gosling():
    say("Я слушаю, чего вы хотели?")
    startListen()


def hello():
    say("Здарова!")


def weather():
    fetchUrl = f"https://api.openweathermap.org/data/2.5/weather?lat={'47.23'}&lon={'39.72'}&lang=ru&appid={OPEN_WEATHER_API_KEY}"

    response = requests.post(url=fetchUrl).json()
    weatherType = f"{response['weather'][0]['description']}"
    windSpeed = f"{response['wind']['speed']} метров в секунду"
    temperature = f"{round(response['main']['temp'] - 273.15, 2)} градусов цельсия"
    temperatureFeelsLike = f"{round(response['main']['feels_like'] - 273.15, 2)} градусов цельсия"
    pressure = f"{response['main']['pressure']} миллиметров ртутного столба"
    humidity = f"{response['main']['humidity']} процентов"
    say(f"сейчас в Ростове-на-Дону {weatherType}, температура: {temperature}, ощущается как {temperatureFeelsLike}, "
        f"скорость ветра: {windSpeed}, давление: {pressure}, влажность: {humidity}")


def joke():
    array = ["А сейчас Анекдот!", "Анекдот!", "А вот и анекдот", "Сейчас шуткану", "Смешнявка"]
    say(array[random.randint(0, len(array) - 1)])
    url = 'http://rzhunemogu.ru/RandJSON.aspx?CType=1'
    text = requests.get(url=url).text
    text = text[12:-2]
    say(text)


def searchInBrowser():
    say("Что нужно найти?")
    text = listen()
    say("Сейчас поищем...")
    for value in ['.com', '.org', '.ru', '.net', '.gov', '.edu', '.info']:
        if value in text:
            webbrowser.open_new(
                f'https://{text}'
            )
            return

    webbrowser.open_new(
        f'https://www.google.com/search?q={text}&aqs=chrome.0.0i355i433i512j46i340i433i512l2j46i433i512j46i512l2j0i512j46i512j0i512j46i512.31386j0j7&sourceid=chrome&ie=UTF-8')