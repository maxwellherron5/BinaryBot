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

            comment.reply(comment_reply + identifyFormat(comment.body))
            print("Replied to comment: " + comment.id)

            comments_replied_to.append(comment.id)

            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

        print("Sleeping for 10 seconds...")
        # Sleep for 10 seconds...
        time.sleep(10)

def identifyFormat(comment):
    output = ""

    for word in comment:
        if isinstance(word, int):
            # output += " " + decToBinary(word)
            output += word
        return str(output)

def testFuction(input):
    output = " "
    for word in input:
        output += str(word)
    return output

def decToBinary(input):
    bit_string = " " + bin(input)
    # This slices the 0b from the output bit string
    output = bit_string[3:len(bit_string)]

    return output


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

