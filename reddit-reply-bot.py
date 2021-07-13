import sys
import traceback
import time
import datetime
import praw

url = "enter the FULL url to the thread you want to focus on"

BOT_USERNAME = 'enter reddit username'
BOT_PASSWORD = 'enter reddit password'
BOT_CLIENT_ID = 'client id'
BOT_CLIENT_SECRET = 'client secret'

def harass():
    reddit = praw.Reddit(username=BOT_USERNAME,
                         password=BOT_PASSWORD,
                         client_id=BOT_CLIENT_ID,
                         client_secret=BOT_CLIENT_SECRET,
                         user_agent='a bot to mess with others')

    submission = reddit.submission(url=url)

    for comment in reddit.redditor("reddit user name you want to reply to on a regular basis").comments.new(limit=None):
        if not comment.saved and "enter the thread id, the unique id per thread" in comment.link_id: #and comment.body == "enter a response you want to focus in on, if you want to focus on a specific phrase": #comment this out to do a mass save of comments first if needed
            print(comment.body.split("\n", 1)[0][:79])
            comment.save() #saves the comment to know which ones it has and has not replied to
            comment.reply('"the reply you want to respond with to the user you are focusing on"') #comment this out if you need to avoid replying right away
            print(submission.id) #this line and bottom line help ensure comments align to the proper thread
            print(comment.link_id)
            print (datetime.datetime.now())
            time.sleep(2)

if __name__ == '__main__':
    while True:
        harass()