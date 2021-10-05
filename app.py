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


@app.route('/', methods=['GET', 'POST'])
def dict_page():
    return render_template('dict.html')


@app.route('/translate', methods=['POST'])
def index_post():
    original_text = request.form['word']
    target_language = "ru"
    print(original_text)
    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']
    path = '/translate?api-version=3.0&'
    target_language_parameter = 'from=en&to=' + target_language
    constructed_url = endpoint + path + target_language_parameter

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = [{'text': original_text}]
    translator_request = requests.post(
        constructed_url, headers=headers, json=body)

    translator_response = translator_request.json()
    translated_text = translator_response[0]['translations'][0]['text']

    return render_template(
        'result.html',
        word=translated_text
    )


'''def dict_page():
    if request.method == 'POST':
        word = request.form["word"]
        return render_template('result.html', word=word)

    return render_template('dict.html')'''


if __name__ == '__main__':
    app.run()
