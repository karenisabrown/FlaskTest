def get_text(sub,count):
    sub_reddit = reddit.subreddit(sub)
    hot_meme = sub_reddit.hot(limit=count)
    result=[]
    textP= "No selftext Present"
    for submission in hot_meme:
        if(submission.selftext):
            temp = {"Title": submission.title,
                    "text": submission.selftext,
                    "Upvotes": submission.ups,
                    "Downvotes": submission.downs,
                    "Redditurl": submission.shortlink,
                    "Subreddit": sub
                    }
        else:
            temp = {"Title": submission.title,
                    "text": textP,
                    "Upvotes": submission.ups,
                    "Downvotes": submission.downs,
                    "Redditurl": submission.shortlink,
                    "Subreddit": sub
                    }

        result.append(temp)
    return result