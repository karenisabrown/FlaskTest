@app.route('/givememe/<sub>')
def custom_meme(sub):
    try:
        r = get_meme(sub,100)

    except:
        return jsonify({
            'Status_code': 404,
            'Message': 'Invalid Subreddit'
        })

    requsted = random.choice(r)

    while not check_image(requsted["Url"]):
        count=count+1
        requsted = random.choice(r)
        if count == 100:
            break

    return jsonify({
        'Title':requsted["Title"],
        'Url': requsted["Url"],
        'Upvotes': requsted["Upvotes"],
        'Downvotes': requsted["Downvotes"],
        'Redditurl': requsted["Redditurl"],
        'Subreddit': requsted["Subreddit"]
    })