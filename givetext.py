@app.route('/givetext/<sub>')
def text_meme(sub):              #showerthoughts or quotes
    r = get_text(sub,100)
    requsted = random.choice(r)

    return jsonify({
        'Title': requsted["Title"],
        'Selftext': requsted["text"],
        'Upvotes': requsted["Upvotes"],
        'Downvotes': requsted["Downvotes"],
        'Redditurl': requsted["Redditurl"],
        'Subreddit': requsted["Subreddit"]
    })