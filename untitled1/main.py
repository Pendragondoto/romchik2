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

a = 1

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print("User: vk.com/id"+str(event.user_id))
        response = event.text.lower()
        if event.from_user and not (event.from_me):
            if response == "тест" and a == 1:
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет, друг!', 'random_id': 0})
                a += 1
            elif response == "тест" and a == 2:
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет, друг! Это уже следующее сообщение', 'random_id': 0})
                a += 1
            elif response == "тест" and a == 3:
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Задолбал уже тестить! Это третье сообщение', 'random_id': 0})
                a += 1

        elif event.from_chat:
            if response == "котики":
                vk_session.method('messages.send', {'chat_id': event.chat_id, 'message': 'Еее', 'random_id': 0})