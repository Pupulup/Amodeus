import kb as kb
import json
import telebot
import requests as req
import os
import logging
import random
import time
import re
from dataclasses import dataclass
from bs4 import BeautifulSoup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from bs4 import BeautifulSoup
import requests
from telebot import TeleBot, types
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests

API_TOKEN = '6018383215:AAF_ROvyrLi9hYmeq2S5LXzhHORzRQDJ_i0'
vafli_group_id = '-1001952449676'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# ПИНГ БОТА
@dp.message_handler(commands=['p'])
async def ping(message: types.Message):
    await message.reply("Я тут")


@dp.message_handler(commands=['all'])
async def all(message: types.Message):
    await message.answer("@Osuuspankk1 @Marrolk @dashe4kin @yayauuyaya")


@dp.message_handler(commands=['h'])
async def helper(message: types.Message):
    await message.answer("/p - пингует бота(чтобы проверять что он точно лежит, а не проблема в коде где-то \n"
                         "/all - тегает всех(в стадии доработки)\n"
                         "/gor - гороскоп")


# ПОГОДА СПБ
open_weather_token = 'fa0456e7c5a170b23b4f0236824c5d7a'
type_weather = {
    "Clear": "Ясно",
    "Clouds": "Облачно",
    "Rain": "Дождь",
    "Drizzle": "Дождь",
    "Thunderstorm": "Гроза",
    "Snow": "Снег ",
    "Mist": "Туман"
}

# ГОРОСКОПЧИК
with open("first.txt", "r", encoding="utf-8") as f1:
    first = f1.readlines()
with open("second.txt", "r", encoding="utf-8") as f2:
    second = f2.readlines()
with open("second_add.txt", "r", encoding="utf-8") as f2_add:
    second_add = f2_add.readlines()
with open("third.txt", "r", encoding="utf-8") as f3:
    third = f3.readlines()


@dp.message_handler(commands=['gor'])
async def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['♈️ Овен ♈️', '♉️ Телец ♉️', '♊️ Близнецы ;3 ♊️', '♋️ Рак ♋️', '♌️ Лев ♌️', '♍️ Дева ♍️', '♎️ Весы ♎️',
               '♏️ Скорпион ♏️', '♐️ Стрелец ♐️', '♑️ Козерог ♑️', '♒️ Водолей ♒️', '♓️ Рыбы ♓️']
    keyboard.add(*buttons)
    await message.answer('Я, конечно, в такое не верю, но дело твое', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "♈️ Овен ♈️" or "♉️ Телец ♉️" or "♊️ Близнецы ;3 ♊️" or
                                    "♋️ Рак ♋️" or "♌️ Лев ♌️" or "♍️ Дева ♍️" or "♎️ Весы ♎️" or "♏️ Скорпион ♏️" or
                                    "♐️ Стрелец ♐️" or "♑️ Козерог ♑️" or "♒️ Водолей ♒️" or "♓️ Рыбы ♓️")
async def oven(message: types.Message):
    msg = random.choice(first) + '' + random.choice(second) + '' + random.choice(second_add) + '' + random.choice(third)
    await message.reply(msg, reply_markup=types.ReplyKeyboardRemove())


# КУРИСУ ОТВЕЧАЕТ)
@dp.message_handler()
async def message_from_users(message: Message):
    dn = ["доброй ночи", "я спать", "спокойной ночи", "сладких снов"]
    mat = ["блять", "сука", "пидор", "пидарас", "пидорас", "бля", "хуй", "пизда", "пиздец", "хуйня", "ебать", "заебало",
           "нахуй", "шлюха", "хуле", "cхуяле", "kurva", "курва", 'хуям']
    # vanya = ["ваня", "иван"]
    buhaem = ["бухаем", "бухаем?", "пьем?", "в кб?", "в кб", "бухать", "пить", "в бар"]
    shutka = ["(шутка)"]
    tilt = ["я в тильте"]
    radost = ["ура!"]
    okno = ["я в окно", "в окно"]
    goroskop = ["гороско курису "]
    if any(item in message.text.lower() for item in dn):
        await message.reply("Добрых снов)")
    elif any(item in message.text.lower() for item in mat):
        await message.reply("Отжимайся!")
    elif any(item in message.text.lower() for item in buhaem):
        await message.reply("ДА!")
    elif any(item in message.text.lower() for item in shutka):
        await message.reply("Не шути больше, у тебя плохо получается")
    elif any(item in message.text.lower() for item in tilt):
        await bot.send_sticker(message.chat.id,
                               "CAACAgUAAxkBAAEIaXNkKEMkiMwJeI0QwszhpMwnPNzqTwACKgkAAnQr4AVa1q3UYDBfOy8E")
    elif any(item in message.text.lower() for item in goroskop):
        await message.reply("Я, конечно, в такое не верю, но дело твое")
    elif any(item in message.text.lower() for item in radost):
        await bot.send_sticker(message.chat.id,
                               "CAACAgUAAxkBAAEIaXpkKESFBPmv-v0AAcm55_ZV2Nq-3oQAAvgIAAJ0K-AFpECLSEAufFEvBA")
    elif any(item in message.text.lower() for item in okno):
        await bot.send_sticker(message.chat.id,
                               "CAACAgUAAxkBAAEIaZVkKEw8r1wQUN5GzDKnURKzJdjJUwACCQkAAnQr4AUYavnANwt75y8E")

    # elif any(item in message.text.lower() for item in vanya):
    #   await message.reply("сдохни")

    # ПОГОДА
    try:
        weather = ["погода", "спб"]
        if any(item in message.text.lower() for item in weather):
            message.text = "Санкт-Петербург"
        else:
            message.text = "hbbfg"
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        temp = data['main']['temp']

        if data["weather"][0]["main"] in type_weather:
            wd = type_weather[data["weather"][0]["main"]]
        else:
            wd = ""
        if wd == 'Дождь':
            umbrl = 'и возьмите зонт'
        else:
            umbrl = ''
        if temp < -25:
            result = 'Там так холодно, лучше останься дома и попей чай'
        if temp < 1:
            result = 'Холодно, одевайся потеплее'
        elif temp < 12:
            result = 'Прохладно'
        elif temp < 25:
            result = 'Тепло'
        else:
            result = 'Жарко'

        await message.reply(f"{result} {umbrl} ({data['main']['temp']}C° {wd})")

    finally:
        return


'''
async def dolgi_timer(bot: Bot):
    start_date = datetime.now()
    flag = False
    while True:
        if datetime.now().hour == start_date.hour:
            flag = False
        r = random.randint(0, 25)
        if r == 0 and not flag:
            await message_sender('@Osuuspankk1, закрывай долги', group_id, bot)
            flag = True
        await asyncio.sleep(3600)
'''

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
