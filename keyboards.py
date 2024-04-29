from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

keyboard = InlineKeyboardMarkup()  # create a keyboard to request "menu"
keyboard.add(InlineKeyboardButton('Все о блокирующих элементах контроля', callback_data='BlockElements'))
keyboard.add(InlineKeyboardButton('Пожаловаться на курс/преподавателя', callback_data='Complaint'))
keyboard.add(InlineKeyboardButton('Что должен содержать ПУД?', callback_data='DisciplineProgram'))
keyboard.add(InlineKeyboardButton('Что такое ПОПАТКУС?', callback_data='Popatkus'))

keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True)  # create a keyboard for the start menu
keyboard2.add(KeyboardButton('Меню'))
keyboard2.add(KeyboardButton('Справка'))
keyboard2.add(KeyboardButton('Оставить обращение'))
keyboard2.add(KeyboardButton('Узнать текущий состав студенческого совета'))
keyboard2.add(KeyboardButton('Хочу в комитет студенческого совета'))

keyboard3 = InlineKeyboardMarkup()  # create a keyboard to request "Leave message"
keyboard3.add(InlineKeyboardButton('Пожаловаться на курс/преподавателя', callback_data='Complaint'))
keyboard3.add(InlineKeyboardButton('Оставить обращение не связанное с этим', callback_data='NotEducationalMessage'))

keyboard4 = InlineKeyboardMarkup()
keyboard4.add(InlineKeyboardButton('Информационный комитет', callback_data='Infocom'))
keyboard4.add(InlineKeyboardButton('Комитет по качеству образования', callback_data='KKO'))
keyboard4.add(InlineKeyboardButton('Комитет по внешним коммуникациям', callback_data='Vneshcom'))
keyboard4.add(InlineKeyboardButton('Социальный комитет', callback_data='Soccom'))
keyboard4.add(InlineKeyboardButton('Я не знаю в какой/хочу в несколько сразу', callback_data='DoNotKnow'))
keyboard4.add(InlineKeyboardButton('Я никуда не хочу, случайно тыкнул', callback_data='Cancel'))