import telebot

bot = telebot.TeleBot('767651930:AAFFQ13qaZuN7SoRKcUGVZ5bPImCWVGIPKs')
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('Понеділок', 'Вівторок', 'Середа','Четвер',"П'ятниця")

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Бота створив:\nInstagram:@denysdovg\nTelegram:@denysdovg', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'понеділок':
        bot.send_message(message.chat.id, '1.Фіз-ра\n2.Укр.мова\n3.Інформатика\n4.Зарубіжна\n5.Укр.літ\n6.Англійська\n7.Мистецтво')
    
    elif message.text.lower() == 'вівторок':
        bot.send_message(message.chat.id, "1.Німецька\n2.Фіз-ра\n3.Укр.мова\n4.Геометрія\n5.Укр.літ\n6.Англійська\n7.Основи Здоров'я")
   
    elif message.text.lower() == 'середа':
       bot.send_message(message.chat.id,
'1.Анлійська\n2.Історія\n3.Німецька\n4.Інформатика\n5.Правознавство\n6.Алгебра\n7.Фіз-ра')
   
    elif message.text.lower() == 'четвер':
      bot.send_message(message.chat.id,
'1.Геометрія\n2.Біологія\n3.Укр.літ\n4.Фізика\n5.Хімія\n6.Георафія')   
    
    elif message.text.lower() == "п'ятниця":
       bot.send_message(message.chat.id,
'1.Історія\n2.Агебра\n3.Фізика\n4.Географія\n5.Зарубіжка\n6.Хімія\n7.Трудове')

bot.polling(none_stop=True)