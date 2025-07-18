import praw
import os
from dotenv import load_dotenv

load_dotenv() 

# Reddit app credentials (do not share these publicly)
reddit = praw.Reddit(
    client_id="x0-s9IIq4QznA0UxhdjK2w",
    client_secret="lz3V0wcKvIlr1m0fxmhvNzhZKrQvmg",
    user_agent="RedstaApp/0.1 by labhesh"
)

def fetch_image_post(subreddit_name):
    sub = reddit.subreddit(subreddit_name)

    for post in sub.hot(limit=100):
        if post.stickied:
            continue

        url = post.url.lower()

        # ✅ Filter valid image links only
        if (
            any(domain in url for domain in ["i.redd.it", "i.imgur.com", "preview.redd.it"])
            and url.endswith((".jpg", ".jpeg", ".png"))
        ):
            return {
                "title": post.title,
                "author": post.author.name if post.author else "unknown",
                "image_url": post.url
            }

    print("❌ No valid image post found in hot list.")
    return None
