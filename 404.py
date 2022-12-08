@app.errorhandler(404)
@app.route('/<lol>')
def not_found(lol):
    return "<h1git >Are You Lost?<h1>"