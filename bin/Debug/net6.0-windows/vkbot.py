# -*- coding: utf-8 -*-

from email import message
import json
import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id


def bot_broadcasting(isHaveNew,albums,geNre,token):

    data = json.load(albums)
    session_a = requests.Session()

    session = vk_api.VkApi(token=token)
    vk_ss = session.get_api()

    longpool = VkLongPoll(session)


    members = vk_ss.groups.getMembers(group_id = '196908223')

    users = members["items"]

    if isHaveNew == False:
        for i in users:
            vk_ss.messages.send(user_id = i,random_id = get_random_id(),message = "Ничего нового не найдено((")
        return

    print(members["count"])

    

    response = "Новыx альбомов в жанре "+ geNre + " : " + str(len(data)) + '\n' + '\n'

    for i in data:
        name = i["Title"]
        genre = i["Genre"]
        date = i["releaseDate"]
        authors = i["Authors"]
        response2 = "Название: " + name + '\n' + "Автор: " + authors + '\n' + "Жанр: " + genre + '\n' +"Дата релиза: " + date +  '\n' + "<________________________>" + '\n'
        response+=response2

    for i in users:
        vk_ss.messages.send(user_id = i,random_id = get_random_id(),message = response)


    