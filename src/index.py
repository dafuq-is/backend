#!/usr/bin/env python3

from bottle import route, run, HTTPResponse
from sources.UrbanDictionary import UrbanDictionary
from sources.Exceptions import NoResultException

@route('/<word>')
def home(word):
    try:
        meaning = UrbanDictionary().getMeaning(word)
    except NoResultException:
        return HTTPResponse(status=404, body="Dafuq! We have no idea what <b>" + word + "</b> is!")

    return HTTPResponse(status=200, body=meaning)

run(host='0.0.0.0', port=8080, debug=True)
