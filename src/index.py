#!/usr/bin/env python3

from bottle import route, run, HTTPResponse
import requests

@route('/<word>')
def home(word):
    word = word
    response = requests.get("http://api.urbandictionary.com/v0/define?term=" + word)
    answer = response.json()
    
    if not answer["list"]:
        response.status = 404
        return HTTPResponse(status=404, body= "Dafuq! Urban Dictionary has no idea what  <b>" + word +"</b> is! ")

    first = answer["list"][0]["definition"]
    response.status = 200
    return first


run(host='0.0.0.0', port=8080, debug=True)
