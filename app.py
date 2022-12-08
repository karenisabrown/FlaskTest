from flask import Flask,jsonify
import random,logging
from main import get_meme, check_image, get_text

app = Flask(__name__)
count = 0
randommeme = ['meme','dankmeme','wholesomeme','memes']

if __name__ == '__main__':
    app.run()
