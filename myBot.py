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
        if "Binary me!" in comment.body:
            print("String with trigger word found in comments!")

            comment_reply = "Hello fellow human! You have triggered the BinaryBot! Your phrase in binary is: "

            comment.reply(comment_reply + identifyFormat(comment))
            print("Replied to comment: " + comment.id)

            comments_replied_to.append(comment.id)

            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

        print("Sleeping for 10 seconds...")
        # Sleep for 10 seconds...
        time.sleep(10)

def identifyFormat(comment):
    output = []

    if isinstance(comment, int):
        output += " " + decToBinary(comment)
    return str(output)


def decToBinary(input):
    # array to store
    # binary number
    binaryNum = [0] * input;

    # counter for binary array
    i = 0;
    while (input > 0):
        # storing remainder
        # in binary array
        binaryNum[i] = input % 2;
        input = int(input / 2);
        i += 1;

    return str(binaryNum)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to


#def toAscii(input):


r = bot_login()
comments_replied_to = get_saved_comments()

while True:
    run_bot(r, comments_replied_to)
