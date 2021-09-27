from flask import Flask, render_template, request
import requests
import os
import uuid
import json
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

my_words = {"hello": "Привет", "car": "Машина", "apple": "Яблоко"}


@app.route('/hello')
def hello_world():
    return "hello world"


@app.route('/hello/<name>')
def hello_with_name(name):
    return f"hello {name}"


# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def dict_page():
    if request.method == 'POST':
        word = request.form["word"]
        return render_template('result.html', word=my_words[word.lower()])

    return render_template('dict.html')


'''def dict_page():
    if request.method == 'POST':
        word = request.form["word"]
        return render_template('result.html', word=word)

    return render_template('dict.html')'''


if __name__ == '__main__':
    app.run()
