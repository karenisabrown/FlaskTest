@app.route('/givetext/<sub>/<int:count>')
def text_count_meme(sub,count):
    if count >= 50:
        return jsonify({
            'status_code': 400,
            'message': 'Please ensure the count is less than 50'
        })

    requested = get_text(sub, 100)
    random.shuffle(requested)


    textmeme = []
    for post in requested:
        if len(textmeme) != count:
            t = {
                'Title': post["Title"],
                'Selftext': post["text"],
                'Upvotes': post["Upvotes"],
                'Downvotes': post["Downvotes"],
                'Redditurl': post["Redditurl"],
                'Subreddit': post["Subreddit"]
            }
            textmeme.append(t)

    return jsonify({
        'sub': textmeme,
        'count': len(textmeme)
    })