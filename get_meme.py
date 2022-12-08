def get_meme(sub,count):
    sub_reddit = reddit.subreddit(sub)
    hot_meme = sub_reddit.hot(limit=count)
    result =[]
    for submissions in hot_meme:
        temp = {"Title": submissions.title,
                  "Url": submissions.url,
                  "Upvotes": submissions.ups,
                  "Downvotes": submissions.downs,
                  "Redditurl": submissions.shortlink,
                  "Subreddit": sub
                  }
        result.append(temp)

    return result