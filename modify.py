#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Bruno Coulet

@file: modify.py
@created: 08/02/2024
@updated 14/02/2024

@project: myDiscord
@licence: GPLv3
"""

"""Ce fichier est appelé par les boutons des interfaces graphiques.
Il appelle à son tour, soit le module message.py, soit user.py, soit channel.py
Ces modules utilise leur méthodes propres (avec du sql) et font appel a db.py"""

from message import Message
from channel import Channel
from user import User
from db import Db



class Modify:
    def __init__(self):
        self.message = Message()
        self.channel = Channel()
        self.user = User()
        self.db = Db()

    def createMessage(self, author_name, channel_id, content):
        try:
            channel_id = int(channel_id)
        except ValueError:
            print("ID de categorie invalide. Veuillez entrer un nombre.")

        self.message.create(author_name, channel_id, content)


    def updateMessage(self, id, id_channel):
        try:
            id = int(id)
        except ValueError:
            print("L'ID de message est invalide. Veuillez entrer un nombre.")
            return

        self.message.update(id, id_channel)


    def deleteMessage(self, id_message):
        """Supprime un message avec l'ID spécifié"""
        try:
            id_message = int(id_message)
        except ValueError:
            print("L'ID de message est invalide. Veuillez entrer un nombre.")
            return

        self.message.delete(id_message)


    def createChannel(self, channel_name, id_channel):
        try:
            id_channel = int(id_channel)
        except ValueError:
            print("ID de categorie invalide. Veuillez entrer un nombre.")

        self.channel.create(channel_name ,id_channel)


    def updateChannel(self, id, id_channel):
        try:
            id = int(id)
        except ValueError:
            print("L'ID de message est invalide. Veuillez entrer un nombre.")
            return

        self.channel.update(id, id_channel)


    def deleteChannel(self):
        """Supprime un message avec l'ID spécifié"""
        id_channel = input("ID de la channel : ")

        try:
            id_channel = int(id)
        except ValueError:
            print("L'ID de message est invalide. Veuillez entrer un nombre.")
            return

        self.channel.delete(id_channel)
    

    def findChannel(self):
        id_channel = input("ID du channel : ")

        try:
            id_channel = int(id_channel)
        except ValueError:
            print("ID de categorie invalide. Veuillez entrer un nombre.")
            # self.menu()

        print(self.channel.find(id_channel))
        # self.menu()

    def addMessageToChannel(self):
        id_message = input("ID du message : ")
        id_channel = input("ID de la channel : ")

        try:
            id_message = int(id_message)
            id_channel = int(id_channel)
        except ValueError:
            print("ID de message ou ID de channel invalide. Veuillez entrer un nombre.")

        self.channel.addMessage(id_message, id_channel)
