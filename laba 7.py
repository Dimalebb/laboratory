import os
import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт, чим можу допомогти?")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

def main():
   bot.infinity_polling()

if __name__ == "__main__":
    main()