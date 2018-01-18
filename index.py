#!/usr/bin/env python3

from bottle import route, run
import requests

@route('/<word>')
def home(word):
    word = word
    response = requests.get("http://api.urbandictionary.com/v0/define?term=" + word)
    answer = response.json()
    first = answer["list"][0]["definition"]
    return first


run(host='localhost', port=8080, debug=True)
