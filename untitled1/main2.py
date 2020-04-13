import sys

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time

token = "4a373555b74bbfe8b382e487c13fc997695fee5eac5783edf3ccad72ca9e3303f296ae74696c831b76029"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)


def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'тест':

        keyboard.add_button('Белая кнопка', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Красная кнопка', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Синяя кнопка', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Привет', color=VkKeyboardColor.PRIMARY)


    elif response == 'привет':
        keyboard.add_button('Тест', color=VkKeyboardColor.POSITIVE)

    elif response == 'котики':
        keyboard.add_button('Котики!', color=VkKeyboardColor.POSITIVE)

    elif response == 'закрыть':
        print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard


def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print('Ссылка на пользователя: vk.com/id'+str(event.user_id))
        response = event.text.lower()
        keyboard = create_keyboard(response)

        if event.from_user and not event.from_me:
            if response == "котики":
                send_message(vk_session, 'user_id', event.user_id, message='Котики огонь!!', keyboard=keyboard)
            elif response == "привет":
                send_message(vk_session, 'user_id', event.user_id, message='Нажми на кнопку, чтобы получить список команд',keyboard=keyboard)
            elif response == "тест":
                send_message(vk_session, 'user_id', event.user_id, message= 'Тестовые команды',keyboard=keyboard)

            elif response=='закрыть':
                send_message(vk_session, 'user_id', event.user_id, message='Закрыть',keyboard=keyboard)

        elif event.from_chat:
            if response == "котики":
                send_message(vk_session, 'chat_id', event.chat_id, message='Держите котиков!')