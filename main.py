import os

import requests
from flask import Flask, send_file, Response, redirect
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def get_pig_latin_url(fact):
    response = requests.post('https://hidden-journey-62459.herokuapp.com/piglatinize/',
        data={'input_text': f'{fact}'}, allow_redirects=False)

    url = response.headers['location']

    return url

@app.route('/')
def home():
    url = get_pig_latin_url(get_fact())

    return f"<a href={url}>{url}</a>"

    #other options for how to display the url
    #return redirect(url)
    #return f'{url}'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

