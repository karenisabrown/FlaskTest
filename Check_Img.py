def check_image(urllink):
    ext = urllink[-4:]
    if ext == '.jpg' or ext == '.png':
        return True

    return False