#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import telebot

bot = telebot.TeleBot(os.environ['ABC:1234'])
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Hi, whats your meme!?")

bot.polling()