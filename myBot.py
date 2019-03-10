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

def run_bot(r, comments_replied_to):
    print("Scanning for trigger statement...")

    for comment in r.subreddit('totallynotrobots').comments(limit=10):
        if "Binary me!" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            comment_reply = "Hello fellow human! You have triggered the BinaryBot! Your phrase in binary is: "



