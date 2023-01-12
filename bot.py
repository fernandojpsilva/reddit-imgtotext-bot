import praw

client_id = ""
client_secret = ""
username = ""
password = ""
user_agent = "<console:ImgToText:1.0>"


reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

subreddit = reddit.subreddit("soccer")

for post in subreddit.hot(limit=10):
    print("*******************************")
    print(post.title)
