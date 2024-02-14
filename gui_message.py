#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Bruno Coulet

@file: gui_message.py
@created: 11/02/2024

@project: myDiscord
@licence: GPLv3
"""
"""                       SCHEMA
            COLUMN 0            COLUMN 1        COLUMN 2

ROW 0       TITLE,              TITLE,          logout button
ROW 1       CHANNEL title,      OLD MESSAGE,    OLD MESSAGE
ROW 2       CHANNEL treeview,   OLD MESSAGE,    OLD MESSAGE
ROW 3       CHANNEL treeview,   NEW MESSAGE,    NEW MESSAGE
ROW 4       CHANNEL treeview,   NEW MESSAGE,    NEW MESSAGE
ROW 5       CHANNEL select,     NEW MESSAGE,    send button

"""


import customtkinter as ctk
from constants import *
from tkinter import ttk
from modify import Modify
# from channel import Channel
# from user import User
# from message import Message

modify = Modify()
author_name = "author_name"
current_channel = "current_channel"

messages =["Message 1", "Message 2", "Message 3", "Message 4", "Message 5", "Message 6","Message 1", "Message 2", "Message 3", "Message 4", "Message 5", "Message 6"]
channels ={
    "Channel 1":["Raoul","Edouard"],
    "Channel 2":["Raoul","Edouard","Jeam-mi"],
    "Channel 3":["Raoul","Edouard"],
    "Channel 4":["Raoul","Edouard"],
    "Channel 5":["Raoul","Edouard"],
    "Channel 6":["Raoul","Edouard"],
    "Channel 7":["Raoul","Edouard"]
}



def view_channels():
    print("view channels")

def create_channel():
    print ("create channel")

# CETTE FONCTION EST MAINTENANT DANS LA CLASSE MESSAGE LIGNE 178 AVEC LE BOUTON DU MêME NOM
# def send_message():
#     modify.createMessage(entry_text.get(), 1)
#     print("send message", entry_text.get())

def log_out():
    print("log out")

def checkbox_callback(self):
        print("checked checkboxes:")


    
class ScrollableFrame(ctk.CTkScrollableFrame):

    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        """To make the MyCheckboxFrame class more dynamically usable, we pass a list of string values to the MyCheckboxFrame, which will be the text values of the checkboxes in the frame. Now the number of checkboxes is also arbitrary."""
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        # self.checkboxes = []

        for i, value in enumerate(self.values):
            label = ctk.CTkLabel(self, text=value)
            label.grid(row=i+1, column=0, padx=10, pady=(10, 0))


    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes


class Message(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Messagerie")
        self.geometry("1200x700")
        self.grid_columnconfigure((0, 1), weight=1)
        self.configure(fg_color="Pale Turquoise3")

        # ----  TITLE -             ROW 0     -------
        title_label = ctk.CTkLabel(self, text=f"Bienvenue dans la messagerie {author_name}", font=(TITLE_FONT))
        title_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        title_label.configure(fg_color="grey25")
        title_label.pack_propagate(False)
        
        # ----  LOGOUT       -      ROW 0 COL 2   ---
        self.button_log_out = ctk.CTkButton(self, text="Se déconnecter", command=log_out)
        self.button_log_out.grid(row=0 , column=2, padx=20, pady=20)




        # ----  CHANNEL -           ROW 1,2,3   COL 0   -------
        self.channel_frame = ctk.CTkFrame(self)
        self.channel_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ns", rowspan=4)
        self.channel_frame.grid_columnconfigure((0, 1), weight=1)
        self.channel_frame.configure(fg_color="Pale Turquoise4")
        
        # ----  CHANNEL / CURRENT - ROW 1.0  COL 0   ---
        self.current_channel_frame = ctk.CTkFrame(self.channel_frame)
        self.current_channel_frame.grid(row=0, column=0, padx=10, pady=(10, 0))
        self.current_channel_frame.configure(fg_color="grey25")
        # title label               ROW 1.0.0    COL 0
        current_channel_label = ctk.CTkLabel(self.current_channel_frame, text=f"Channel actuel : {current_channel}", font=SUBTITLE_FONT)
        current_channel_label.grid(row=0, column=0, padx=20, pady=20)
        # title value               ROW 1.0.1    COL 0
        current_channel_title = ctk.CTkLabel(self.current_channel_frame, text="Les courges ont encore augmentées.", font=FONT, wraplength=200)
        current_channel_title.grid(row=1, column=0, padx=20, pady=20)

        # ----  CHANNEL / OTHER  -  ROW 1.1 and 1.3    COL 0  
        # Création du Treeview pour afficher les channels
        self.channel_tree = ttk.Treeview(self.current_channel_frame)
        # self.channel_tree = ttk.Treeview(self.current_channel_frame, columns=("Channel"))
        self.channel_tree.heading("#0", text="Autre channels")
        self.channel_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", rowspan=3)
        # Ajout des channels au Treeview
        self.add_channels_to_tree(channels)




        # ----  CHANNEL FRAME - create_channel ROW 1.4  COL 0
        self.button_create_channel = ctk.CTkButton(self.channel_frame, text="Créer un channel", command=create_channel)
        self.button_create_channel.grid(row=4, column=0, padx=20, pady=20, sticky="s")




        # ----  EXISTANT MESSAGES -  ROW 1 and 2  COL 1 and 2
        self.frame_old_message = ScrollableFrame(self, "Messages existants", values=[message for message in messages])
        self.frame_old_message.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="ew", columnspan=2, rowspan=2)
        self.frame_old_message.configure(fg_color="Pale Turquoise4")
        self.frame_old_message.pack_propagate(False)
      

        # ----  NEW MESSAGE FRAME  - ROW 3    COL 1 and 2    ---
        self.message_frame = ctk.CTkFrame(self)
        self.message_frame.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="ew", columnspan=2, rowspan=2)
        self.message_frame.grid_columnconfigure((0, 1), weight=1)
        self.message_frame.grid_rowconfigure((0, 1), weight=1)
        self.message_frame.configure(fg_color="Pale Turquoise4")

        # -------- label  -     ROW 3.0    COL 0 and 1    ---
        new_message_label = ctk.CTkLabel(self.message_frame, text="Nouveau Message.", font=SUBTITLE_FONT)
        new_message_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        new_message_label.configure(fg_color="grey25")
        # -------- is text  -   ROW 3.1    COL 0    ---
        self.checkbox_text_message = ctk.CTkCheckBox(self.message_frame, text="Message texte")
        self.checkbox_text_message.grid(row=1, column=0, padx=20, pady=(20, 20), sticky="w")
        # -------- is audio  -  ROW 3.1    COL 1    ---
        self.checkbox_audio_message = ctk.CTkCheckBox(self.message_frame, text="Message audio")
        self.checkbox_audio_message.grid(row=1, column=1, padx=20, pady=(20, 20), sticky="w")
        # --------  input area
        entry_text = ctk.CTkEntry(self.message_frame, width=600, height=100,)
        entry_text.grid(row=2, column=0, padx=10, pady=10)
        entry_text.configure(fg_color="Pale Turquoise4")
        # -------- send message button
        def send_message():
            modify.createMessage(author_name="author_name", channel_id=1, content=entry_text.get())
            print("send message", entry_text.get())

        self.button_send_message = ctk.CTkButton(self.message_frame, text="Publier le message", command=lambda: send_message())
        self.button_send_message.grid(row=3, column=0, padx=20, pady=20)


    def  checkbox_callback(self):
        print("checkboxes sélectionnées:", self.checkbox_frame_old_message.get())

    def add_channels_to_tree(self, channels):
        for channel, users in channels.items():
            # Insérer le channel dans le Treeview
            channel_node = self.channel_tree.insert("", "end", text=channel, values=(channel))
            # Ajouter les utilisateurs sous le channel
            for user in users:
                self.channel_tree.insert(channel_node, "end", text=user)

            # Créer un style personnalisé pour le Treeview avec la couleur de fond souhaitée
        # style = ttk.Style()
        # style.configure("Custom.Treeview", background="Pale Turquoise4")  # Remplacez "Pale Turquoise4" par la couleur souhaitée
        # # Appliquer ce style au Treeview
        # self.channel_tree.configure(style="Custom.Treeview")

        # # Créer un style personnalisé pour le Treeview avec la couleur de fond souhaitée
        # style = ttk.Style()
        # style.configure("Custom.Treeview", background="Pale Turquoise4", fieldbackground="Pale Turquoise4")
        # # Appliquer ce style au Treeview
        # self.channel_tree.configure(style="Custom.Treeview")

        #     # Modifier la couleur de fond de l'en-tête
        # self.channel_tree.heading("#0", background="Pale Turquoise4", foreground="white")


message = Message()
message.mainloop()
