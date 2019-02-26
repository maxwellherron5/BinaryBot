'''
    File name: myBot.py
    Author: Maxwell Herron
    Date Created: 02/25/2019
    Program Description: This program runs a bot on Reddit that passively listens for users
    in the comments section to use a phrase to trigger it. Upon being triggered, it will convert
    whatever they say after the activation statement to binary, and then reply to them with the binary statement.
'''

import praw
import config
import time
import os
import requests

# This function is responsible for actually logging the bot in
def bot_login():
    print("Loggin in...")
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "My binary conversion bot!")
    print("Logged in!")
    return r



