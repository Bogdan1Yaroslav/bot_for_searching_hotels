import telebot
from decouple import config
from peewee import *

bot = telebot.TeleBot(config('Token'))

headers: dict = {
    'x-rapidapi-host': "hotels4.p.rapidapi.com",
    'x-rapidapi-key': config('Rapid_API_KEY')
}

my_db = MySQLDatabase(
    config("DB_name"),
    user="root",
    password=config("DB_password"),
    host='localhost',
    port=int(config("DB_port"))

)
