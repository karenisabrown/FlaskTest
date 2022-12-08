@app.route('/givememe/<int:c>')
def multiple(c):
    sub = random.choice(randommeme)

    if c >= 50:
        return jsonify({
            'status_code': 400,
            'message': 'Ensure that the Count is less than 50'
        })

    requested = get_meme(sub, 100)

    random.shuffle(requested)

    memes = []
    for post in requested:
        if check_image(post["Url"]) and len(memes) != c:

            t = {
                'Title': post["Title"],
                'Url': post["Url"],
                'Upvotes': post["Upvotes"],
                'Downvotes': post["Downvotes"],
                'Redditurl': post["Redditurl"],
                'Subreddit': post["Subreddit"]
            }
            memes.append(t)


    return jsonify({
        'memes': memes,
        'count': len(memes)
        })