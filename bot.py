import telebot
from telebot import types
       
token = '8495971064:AAHFlqhm3ZZVcqCnOQLjMxXVK-N4B-4PtX0'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Начать')
    markup.add(button1)
    bot.send_message(message.chat.id, '💜Добро пожаловать в бот расписания кружков УУНиТ💜', reply_markup=markup)

@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Начать')
    markup.add(button1)

#добавляем кружки
#Танцы
dance_ensemble_yeshlek = '1) Ансамбль народного танца «Йешлек»'
dance_ensemble_allegro = '2) Ансамбль спортивного бального танца «Аллегро»'
dance_ensemble_irandek = '3) Заслуженный коллектив народного творчества РБ Народный ансамбль танца «Ирандек»'
#Пение
song_septima = '1) Вокальная студия «Септима»'
song_moment_more = '2) Кавер-группа «Моментов море»'
song_aktamir = '3) Народный ансамбль кураистов «Актамыр»'
#Театр
teatr_oskon = '1) Башкирский народный студенческий театр "Оскон"("Искра")'
teatr_grotesk = '2) Русский студенческий театр "Гротекс"'
teatr_selet = '3) Татарский музыкально-поэтический театр "Сэлэт"(Талант")'
#Спорт
sport_green = '1) Зеленый проект'
sport_voshod = '2) Туристический клуб "Восхождение"'
sport_ikar = '3) Туристический клуб «Икар»'
#По интересам
anime = '1) Аниме клуб «Аматэрасу»'
math_club = '2) Математический клуб УУНиТ'

user_states = {}
@bot.message_handler(content_types='text')
def message_reply(message):
    user_id = message.from_user.id
    current_section = user_states.get(user_id, 0)

    if message.text == 'Начать':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Танцы')
        button2 = types.KeyboardButton('Пение')
        button3 = types.KeyboardButton('Театр')
        button4 = types.KeyboardButton('Спорт')
        button5 = types.KeyboardButton('По интересам')
        markup.add(button1, button2, button3, button4, button5)
        bot.send_message(message.chat.id, 'Выберите направление кружка:', reply_markup=markup)
        #обнуляем значение
        user_states[user_id] = 0

    elif message.text in ['Танцы', 'Пение', 'Театр', 'Спорт', 'По интересам']:
        # Здесь можно добавить логику для каждого направления
        if message.text == 'Танцы':
            current_section = 1
            user_states[user_id] = 1
            bot.send_message(message.chat.id, f'🕺 Танцевальные кружки:\n {dance_ensemble_yeshlek}\n {dance_ensemble_allegro}' \
            f'\n {dance_ensemble_irandek}')
        elif message.text == 'Пение':
            current_section = 2
            user_states[user_id] = 2
            bot.send_message(message.chat.id, f'🎤 Вокальные кружки:\n {song_septima}\n {song_moment_more}'
            f'\n {song_aktamir}')
        elif message.text == 'Театр':
            current_section = 3
            user_states[user_id] = 3
            bot.send_message(message.chat.id, f'🎨 Театральные кружки:\n {teatr_oskon}\n {teatr_grotesk}' \
            f'\n {teatr_selet}')
        elif message.text == 'Спорт':
            current_section = 4
            user_states[user_id] = 4
            bot.send_message(message.chat.id, f'⚽ Спортивные кружки:\n {sport_green}\n {sport_voshod}\n {sport_ikar}')
        elif message.text == 'По интересам':
            current_section = 5
            user_states[user_id] = 5
            bot.send_message(message.chat.id, f'🎯 Кружки по интересам:\n {anime}\n {math_club}')


        # Добавляем кнопку для возврата
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        button6 = types.KeyboardButton('Выбрать кружок')
        markup.add(back_button, button6)
        bot.send_message(message.chat.id, 'Выберите следующее действие:', reply_markup=markup)

    elif message.text == 'В главное меню':
        user_states[user_id] = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Начать')
        markup.add(button1)
        bot.send_message(message.chat.id, 'Возврат в главное меню', reply_markup=markup)

    elif message.text == 'Выбрать кружок':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button7 = types.KeyboardButton('1)')
        button8 = types.KeyboardButton('2)')
        button9 = types.KeyboardButton('3)')
        markup.add(button7, button8, button9)
        bot.send_message(message.chat.id, 'Какой кружок вам интересен?', reply_markup=markup)


    if current_section == 1 and message.text == '1)':
        bot.send_message(message.chat.id, f'{dance_ensemble_yeshlek}')
    elif current_section == 1 and message.text == '2)':
        bot.send_message(message.chat.id, f'{dance_ensemble_allegro}')
    elif current_section == 1 and message.text == '3)':
        bot.send_message(message.chat.id, f'{dance_ensemble_irandek}')

    elif current_section == 2 and message.text == '1)':
        bot.send_message(message.chat.id, f'{teatr_oskon}')
    elif current_section == 2 and  message.text == '2)':
        bot.send_message(message.chat.id, f'{teatr_grotesk}')
    elif current_section == 2 and message.text == '3)':
        bot.send_message(message.chat.id, f'{teatr_selet}')

    elif current_section == 3 and message.text == '1)':
        bot.send_message(message.chat.id, f'{song_septima}')
    elif current_section == 3 and message.text == '2)':
        bot.send_message(message.chat.id, f'{song_moment_more}')
    elif current_section == 3 and message.text == '3)':
        bot.send_message(message.chat.id, f'{song_aktamir}')

    elif current_section == 4 and message.text == '1)':
        bot.send_message(message.chat.id, f'{sport_green}')
    elif current_section == 4 and message.text == '2)':
        bot.send_message(message.chat.id, f'{sport_voshod}')
    elif current_section == 4 and message.text == '3)':
        bot.send_message(message.chat.id, f'{sport_ikar}')

    elif current_section == 5 and message.text == '1)':
        bot.send_message(message.chat.id, f'{anime}')
    elif current_section == 5 and message.text == '2)':
        bot.send_message(message.chat.id, f'{math_club}')
    '''else:
        bot.send_message(message.chat.id, 'Пожалуйста, используйте кнопки для навигации')'''

if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()