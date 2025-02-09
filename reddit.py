import pandas as pd
import praw
from datetime import datetime
import os
# from dotenv import load_dotenv
# load_dotenv()


class RedditBot():
    def __init__(self):
        self.start()

    def start(self):
        CLIENT_ID = "5xT_cF4FCo3fh8nzeSHYAQ"
        SECRET_KEY = "GkPEMvWkIUJ5n_VIiTcMjqUxxNFpgQ"

        user_agent = "scrapper"
        self.reddit = praw.Reddit(client_id=CLIENT_ID,
                                  client_secret=SECRET_KEY,
                                  user_agent=user_agent
                                  )

    def returnPosts(self, max_chars=1300):
        posts = []
        ml_subreddit = self.reddit.subreddit('AmItheAsshole')
        for i, post in enumerate(ml_subreddit.hot(limit=50)):
            if i == 0:
                continue
            if len(post.selftext) > max_chars:
                continue
            posts.append({"title": post.title,
                          "score": post.score, "id": post.id, "comments": post.num_comments, "chars": len(post.selftext), "text": post.selftext, "created": (datetime.now()-datetime.fromtimestamp(post.created)).total_seconds() / 3600})

        return posts
    

def choose_post():
    bot = RedditBot()
    posts = bot.returnPosts()
    print(pd.DataFrame(posts))
    choice = int(input())
    try:
        print(posts[choice]["title"])
        print(posts[choice]["text"])
        return (True, posts[choice]["title"], posts[choice]["text"])
    except:
        return (False, -1, -1)
    
# choose_post()