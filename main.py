import telebot
from telebot import types
import os
from dotenv import load_dotenv
import requests
import random
import schedule
import time

from threading import Thread

from keyboards import keyboard, keyboard2, keyboard3, keyboard4
from texts import texts

load_dotenv()

GIPHY_TOKEN = os.environ.get('GIPHY')
PIXABAY = os.environ.get('PIXABAY')
UNSPLASH = os.environ.get('UNSPLASH')
ADMIN_CHAT_ID = int(os.environ.get('ADMIN_CHAT_ID'))
bot = telebot.TeleBot(os.environ.get('TELEGRAM_TOKEN'))

active_users = []  # create an array of bot users


@bot.message_handler(commands=['start'])
def start_message(message):  # function that is called when the bot starts
    user_id = message.from_user.id  # extract user id
    if user_id not in active_users:  # if the user is new, add him to the array
        active_users.append(user_id)
    bot.send_message(message.chat.id, texts['start'],
                     reply_markup=keyboard2)


@bot.message_handler(func=lambda message: message.text == "Узнать текущий состав студенческого совета")
def studsovet(message: types.Message):  # who related to GSB counsil
    bot.reply_to(message, texts['compound'], disable_web_page_preview=True)


@bot.message_handler(func=lambda message: message.text == "Меню")
def show_menu(message: types.Message):  # offer the user a selection menu after texting "Меню"
    bot.reply_to(message, "Выбери команду:", reply_markup=keyboard)


@bot.message_handler(commands=["menu"])
def show_menu(message: types.Message):  # offer the user a selection menu after texting "/menu"
    bot.reply_to(message, "Выбери команду:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Справка")
def help(message: types.Message):  # a function that will tell the user about the bot's capabilities
    bot.reply_to(message, texts['help'])


@bot.message_handler(commands=["help"])
def help(message: types.Message):  # the same function is only called using /help
    bot.reply_to(message, texts['help'])


@bot.callback_query_handler(func=lambda call: call.data == "BlockElements")
def block_elements(call):  # a function that sends the user information about blocking controls
    bot.send_message(call.message.chat.id, texts['block'])


@bot.callback_query_handler(func=lambda call: call.data == "DisciplineProgram")
def discipline_program(call):  # a function that sends the user information about discipline program
    bot.send_message(call.message.chat.id, texts['pud'])


@bot.callback_query_handler(func=lambda call: call.data == "Popatkus")
def popatkus(call):  # a function that sends the user information about popatkus
    bot.send_message(call.message.chat.id, texts['popatkus'])
    # send_kitten_photo(call.message.chat.id)


@bot.message_handler(func=lambda message: message.text == "Хочу в комитет студенческого совета")
def wants_to_ss(message: types.Message):
    bot.reply_to(message, "Выбери комитет, куда бы ты хотел пойти", reply_markup=keyboard4)


@bot.callback_query_handler(func=lambda call: call.data == 'Infocom')
def end1(call):
    if call.from_user.username:  # Если у пользователя есть username
        admin_message = f"Пользователь хочет в инфоком: @{call.from_user.username}\n\n"
        bot.send_message(ADMIN_CHAT_ID, admin_message)  # Отправляем сообщение администратору
        bot.send_message(call.from_user.id, "Спасибо, скоро мы с тобой свяжемся!")
    else:  # Если username отсутствует, запрашиваем номер телефона
        msg = bot.send_message(call.from_user.id, "Пожалуйста, укажи свой номер телефона для связи:")
        bot.register_next_step_handler(msg, handle_phone_for_infocom)  # Переходим к обработке номера телефона


def handle_phone_for_infocom(message):
    phone_number = message.text  # Предполагаем, что пользователь ввел номер телефона
    admin_message = f"Пользователь хочет в инфоком, контактный номер: {phone_number}\n\n"
    bot.send_message(ADMIN_CHAT_ID, admin_message)  # Отправляем сообщение администратору
    bot.send_message(message.chat.id, "Спасибо, скоро мы с тобой свяжемся!")


@bot.callback_query_handler(func=lambda call: call.data == 'KKO')
def end2(call):
    if call.from_user.username:  # Если у пользователя есть username
        admin_message = f"Пользователь хочет в KKO: @{call.from_user.username}\n\n"
        bot.send_message(ADMIN_CHAT_ID, admin_message)  # Отправляем сообщение администратору
        bot.send_message(call.from_user.id, "Спасибо, скоро мы с тобой свяжемся!")
    else:  # Если username отсутствует, запрашиваем номер телефона
        msg = bot.send_message(call.from_user.id, "Пожалуйста, укажи свой номер телефона для связи:")
        bot.register_next_step_handler(msg, handle_phone_for_KKO)  # Переходим к обработке номера телефона


def handle_phone_for_KKO(message):
    phone_number = message.text  # Предполагаем, что пользователь ввел номер телефона
    admin_message = f"Пользователь хочет в KKO, контактный номер: {phone_number}\n\n"
    bot.send_message(ADMIN_CHAT_ID, admin_message)  # Отправляем сообщение администратору
    bot.send_message(message.chat.id, "Спасибо, скоро мы с тобой свяжемся!")


@bot.callback_query_handler(func=lambda call: call.data == 'Vneshcom')
def end3(call):
    if call.from_user.username:  # Если у пользователя есть username
        admin_message = f"Пользователь хочет во внешком: @{call.from_user.username}\n\n"
        bot.send_message(ADMIN_CHAT_ID, admin_message)  # Отправляем сообщение администратору
        bot.send_message(call.from_user.id, "Спасибо, скоро мы с тобой свяжемся!")
    else:  # Если username отсутствует, запрашиваем номер телефона
        msg = bot.send_message(call.from_user.id, "Пожалуйста, укажи свой номер телефона для связи:")
        bot.register_next_step_handler(msg, handle_phone_for_vneshcom)  # Переходим к обработке номера телефона


def handle_phone_for_vneshcom(message):
    phone_number = message.text  # Предполагаем, что пользователь ввел номер телефона
    admin_message = f"Пользователь хочет во внешком, контактный номер: {phone_number}\n\n"
    bot.send_message(ADMIN_CHAT_ID, admin_message)  # Отправляем сообщение администратору
    bot.send_message(message.chat.id, "Спасибо, скоро мы с тобой свяжемся!")


@bot.callback_query_handler(func=lambda call: call.data == 'Soccom')
def end4(call):
    if call.from_user.username:  # Если у пользователя есть username
        admin_message = f"Пользователь хочет в соцком: @{call.from_user.username}\n\n"
        bot.send_message(ADMIN_CHAT_ID, admin_message)  # Отправляем сообщение администратору
        bot.send_message(call.from_user.id, "Спасибо, скоро мы с тобой свяжемся!")
    else:  # Если username отсутствует, запрашиваем номер телефона
        msg = bot.send_message(call.from_user.id, "Пожалуйста, укажи свой номер телефона для связи:")
        bot.register_next_step_handler(msg, handle_phone_for_soccom)  # Переходим к обработке номера телефона


def handle_phone_for_soccom(message):
    phone_number = message.text  # Предполагаем, что пользователь ввел номер телефона
    admin_message = f"Пользователь хочет в соцком, контактный номер: {phone_number}\n\n"
    bot.send_message(ADMIN_CHAT_ID, admin_message)  # Отправляем сообщение администратору
    bot.send_message(message.chat.id, "Спасибо, скоро мы с тобой свяжемся!")


@bot.callback_query_handler(func=lambda call: call.data == 'DoNotKnow')
def end5(call):
    if call.from_user.username:  # Если у пользователя есть username
        admin_message = f"Пользователь хочет в студсовет. Надо уточнить куда: @{call.from_user.username}\n\n"
        bot.send_message(ADMIN_CHAT_ID, admin_message)  # Отправляем сообщение администратору
        bot.send_message(call.from_user.id, "Спасибо, скоро мы с тобой свяжемся!")
    else:  # Если username отсутствует, запрашиваем номер телефона
        msg = bot.send_message(call.from_user.id, "Пожалуйста, укажи свой номер телефона для связи:")
        bot.register_next_step_handler(msg, handle_phone)  # Переходим к обработке номера телефона


def handle_phone(message):
    phone_number = message.text  # Предполагаем, что пользователь ввел номер телефона
    admin_message = f"Пользователь хочет в студсовет. Надо уточнить куда, контактный номер: {phone_number}\n\n"
    bot.send_message(ADMIN_CHAT_ID, admin_message)  # Отправляем сообщение администратору
    bot.send_message(message.chat.id, "Спасибо, скоро мы с тобой свяжемся!")


@bot.callback_query_handler(func=lambda call: call.data == 'Cancel')
def cancel(call):
    bot.send_message(call.from_user.id, "Мы все равно будем очень тебя ждать!")


# def send_photo(chat_id):  # function that send photo to user with ID char_id
#     url = "https://api.unsplash.com/photos/random"
#     params = {
#         "client_id": UNSPLASH,  # API-key
#         "query": "morning"  # photo related to morning
#     }
#     response = requests.get(url, params=params)
#     photo_data = response.json()  # data from request
#     photo_url = photo_data.get("urls", {}).get("regular")  # get photo URL
#     if photo_url:
#         bot.send_photo(chat_id, photo_url)  # send this photo to user


# def send_kitten_photo(chat_id):  # this function work only with turn on VPN
#     url = "https://pixabay.com/api/"
#     api_key = PIXABAY  # API-key
#     query = "kitten"
#     params = {
#         "key": api_key,
#         "q": query,
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
#     random_number = random.randint(0, len(data) - 1)  # choose random photo
#     photo_url = data["hits"][random_number]["webformatURL"]  # photo URL
#     bot.send_photo(chat_id, photo_url)  # send photo to user


def send_gif(chat_id):  # function that send gif to user with ID char_id
    url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": GIPHY_TOKEN,  # API-key
        "q": "cat",  # photo related to cats
        "rating": "g"
    }
    response = requests.get(url, params=params)
    data = response.json().get("data")  # get data from response
    random_number = random.randint(0, len(data) - 1)
    gif_data = data[random_number]  # get random gif from data
    gif_url = gif_data.get("images", {}).get("original", {}).get(
        "url")  # get URL-animation
    if gif_url:
        bot.send_animation(chat_id, gif_url)  # send gif to user


@bot.message_handler(func=lambda message: message.text == "Оставить обращение")
# if user wants to leave a message, he is prompted to select the type of problem
def leave_request(message: types.Message):
    bot.reply_to(message, "Выбери тип проблемы, которую ты хочешь описать", reply_markup=keyboard3)



@bot.message_handler(commands=["leaveMessage"])
def leave_request(message: types.Message):
    bot.reply_to(message, "Выбери тип проблемы, которую ты хочешь описать", reply_markup=keyboard3)



@bot.callback_query_handler(func=lambda call: call.data == 'NotEducationalMessage')
def not_educational_message(call):  # if the user wants to leave a request not related to the educational process
    chat_id = call.message.chat.id
    bot.send_message(chat_id,
                     "Опиши свою проблему или оставьте обращение. Если не хочешь писать обращение, напиши \"отмена\"")
    bot.register_next_step_handler(call.message, end_of_message)  # moving on to the next step of function


def end_of_message(message):
    chat_id = message.chat.id  # read the user ID
    if message.text.lower() == "отмена":  # check if user wants to cancel
        bot.send_message(chat_id, "Процесс жалобы отменён.")
        return  # exit the function to stop further processing
    complaint = message.text  # read text of message

    if message.chat.username:  # if username exists
        bot.send_message(chat_id, "Мы обязательно рассмотрим твое сообщение и вернемся с ответом!")
        send_gif(chat_id)  # send a gif
        admin_message = f"Проблема у пользователя @{message.chat.username}:\n\n" \
                        f"Проблема: {complaint}"
        bot.send_message(ADMIN_CHAT_ID, admin_message)  # send message to @tusha_ches
    else:  # if no username, ask for phone number
        msg = bot.send_message(chat_id, "Пожалуйста, укажи свой номер телефона для связи:")
        bot.register_next_step_handler(msg, handle_phone_number, complaint)


def handle_phone_number(message, complaint):
    chat_id = message.chat.id
    phone_number = message.text  # assuming user inputs valid phone number
    bot.send_message(chat_id,
                     "Мы обязательно рассмотрим твое сообщение и вернемся с ответом!")
    send_gif(chat_id)  # send a gif
    admin_message = f"Проблема у пользователя с номером {phone_number}:\n\n" \
                    f"Проблема: {complaint}"
    bot.send_message(ADMIN_CHAT_ID, admin_message)  # send message to @tusha_ches


@bot.callback_query_handler(func=lambda call: call.data == "Complaint")
def start_complaint(call):  # function for educational problems
    chat_id = call.message.chat.id  # read the user ID
    bot.send_message(chat_id, "Введи имя преподавателя или напиши \"отмена\":")
    bot.register_next_step_handler(call.message, get_teacher_name)  # move on the next step


def get_teacher_name(message):
    chat_id = message.chat.id
    if message.text.lower() == "отмена":  # check if user wants to cancel
        bot.send_message(chat_id, "Процесс жалобы отменён.")
        return  # exit the function to stop further processing
    teacher_name = message.text  # read the teacher name from the message
    bot.send_message(chat_id, "Введи название курса или напиши \"отмена\":")
    bot.register_next_step_handler(message, lambda msg: get_course_name(msg, teacher_name))  # move on the next step


def get_course_name(message, teacher_name):
    chat_id = message.chat.id
    if message.text.lower() == "отмена":  # check if user wants to cancel
        bot.send_message(chat_id, "Процесс жалобы отменён.")
        return  # exit the function to stop further processing
    course_name = message.text  # read the course name
    bot.send_message(chat_id,
                     "На каком курсе ты учишься? (Например, 1 курс бакалавриата). Если не хочешь писать жалобу, напиши \"отмена\"")
    # move on the next step
    bot.register_next_step_handler(message, lambda msg: get_course(msg, teacher_name, course_name))


def get_course(message, teacher_name, course_name):
    chat_id = message.chat.id
    if message.text.lower() == "отмена":  # check if user wants to cancel
        bot.send_message(chat_id, "Процесс жалобы отменён.")
        return  # exit the function to stop further processing
    course = message.text  # save the course of user
    bot.send_message(chat_id, "На какой программе ты обучаешься? (Например, бизнес-информатика)."
                              " Если не хочешь писать жалобу, напиши \"отмена\"")
    bot.register_next_step_handler(message, lambda msg: get_program(msg, teacher_name, course_name, course))


def get_program(message, teacher_name, course_name, course):
    chat_id = message.chat.id
    if message.text.lower() == "отмена":  # check if user wants to cancel
        bot.send_message(chat_id, "Процесс жалобы отменён.")
        return  # exit the function to stop further processing
    program_name = message.text  # save the educational course of user
    bot.send_message(chat_id, "Оставь жалобу или напиши \"отмена\":")
    bot.register_next_step_handler(message,
                                   lambda msg: get_complaint(msg, teacher_name, course_name, program_name, course))


# this function ends educational complaint of user
def get_complaint(message, teacher_name, course_name, program_name, course):
    chat_id = message.chat.id  # read user ID
    if message.text.lower() == "отмена":  # check if user wants to cancel
        bot.send_message(chat_id, "Процесс жалобы отменён.")
        return  # exit the function to stop further processing

    complaint = message.text  # read text of complaint
    if message.chat.username:  # check if username exists
        bot.send_message(chat_id, "Мы обязательно рассмотрим твое сообщение и вернемся с ответом!")  # send response
        send_gif(chat_id)  # send gif
        admin_message = f"Жалоба от пользователя @{message.chat.username}:\n\n" \
                        f"Преподаватель: {teacher_name}\n" \
                        f"Название курса: {course_name}\n" \
                        f"Программа обучения: {program_name}\n" \
                        f"Курс обучения: {course}\n" \
                        f"Жалоба: {complaint}"
        bot.send_message(ADMIN_CHAT_ID, admin_message)  # send complaint to admin
    else:  # if no username, ask for phone number
        msg = bot.send_message(chat_id, "Пожалуйста, укажи свой номер телефона для связи:")
        bot.register_next_step_handler(msg, handle_phone_number_complaint, teacher_name, course_name, program_name,
                                       course, complaint)


def handle_phone_number_complaint(message, teacher_name, course_name, program_name, course, complaint):
    chat_id = message.chat.id
    phone_number = message.text  # assuming user inputs valid phone number
    bot.send_message(chat_id,
                     "Мы обязательно рассмотрим твое сообщение и вернемся с ответом!")
    send_gif(chat_id)  # send gif
    admin_message = f"Жалоба от пользователя с номером {phone_number}:\n\n" \
                    f"Преподаватель: {teacher_name}\n" \
                    f"Название курса: {course_name}\n" \
                    f"Программа обучения: {program_name}\n" \
                    f"Курс обучения: {course}\n" \
                    f"Жалоба: {complaint}"
    bot.send_message(ADMIN_CHAT_ID, admin_message)  # send complaint to admin


# def new_day():  # sends a message "Доброе утро!" every morning
#     for chat_id in active_users:  # send to all users who launched the bot
#         bot.send_message(chat_id, "Доброе утро!")
#         send_photo(chat_id)
#         time.sleep(1)  # pause between sending messages


def scheduler_polling():
    while True:
        schedule.run_pending()
        time.sleep(1)


# schedule.every().day.at('10:00').do(new_day)  # schedule to call function new day every day at 10 am

# we create a new execution thread that runs the scheduler_polling function
Thread(target=scheduler_polling).start()

# we initiate the process of continuously polling Telegram servers for new messages or events
bot.infinity_polling()
