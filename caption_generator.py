def generate_caption(title, author, subreddit):
    default_tags = "#explorepage #trending"

    hashtag_sets = {
        "cars": "#carstagram #modifiedcars #carlovers #jdm",
        "memes": "#memes #funny #memeoftheday #dankmemes",
        "photography": "#aesthetic #naturelovers #photooftheday",
        "gaming": "#gamer #gamingmemes #pcgaming #xbox #playstation",
    }

    hashtags = hashtag_sets.get(subreddit.lower(), default_tags)

    caption = (
        f"🔥 {title}\n"
        f"📸 via u/{author} on r/{subreddit}\n\n"
        f"{hashtags}"
    )
    return caption
    