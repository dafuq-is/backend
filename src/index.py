#!/usr/bin/env python3

import random
import os

from bottle import route, run, HTTPResponse
from sources.Exceptions import NoResultException, SourceNotFound
from fetcher import fetchFirstMeaning

from sources import Factory


@route('/')
def main():
    intro_file = os.getcwd() + "/src/intro.html"
    html = open(intro_file, "r")
    return HTTPResponse(status=200, body=html.read())


@route('/<word>')
def get_meaning(word):
    _prioritizedSources = Factory.getAllSources()

    # randomize (for now)
    # The idea is to create a prioritized list based on the word
    # A smart system that selects the likeliness of people looking for a specific source
    # when they think of the word.
    # e.g., when someone says fudge, they might be more like to find that its a replacement of f***
    # rather than looking for a candy.
    #
    # We will categorize the sources based on what kind of meaning it provides (literal, pop culture, meme, etc)
    # ...and find association of the particular word or phrase with these categories
    #
    # Each source within a category will be separately ranked
    # One source can be in more than one category with different ranks
    random.shuffle(_prioritizedSources)

    try:
        meaning = fetchFirstMeaning(_prioritizedSources, word)
    except NoResultException:
        return HTTPResponse(status=404, body="Dafuq! <b>" + word +  "</b> is not known to any of our sources")

    return HTTPResponse(status=200, body=meaning['meaning'] + '.<br><br>as defined by: <b>' + meaning['source'] + '</b>')


@route('/<word>/<service>')
def choose(word, service):
    try:
        meaning = Factory.getSource(service).getMeaning(word)
    except NoResultException:
        return HTTPResponse(status=404, body="Dafuq! <b>" + service + "</b> does not know about <b>" + word + "</b>! ")
    except SourceNotFound:
        supported = ", ".join(Factory.getAllSources())
        return HTTPResponse(status=404, body="Dafuq! <b>" + service + "</b> is not supported. Use: <i>" + supported + "</i>!")

    return HTTPResponse(status=200, body=meaning)


run(host='0.0.0.0', port=8080, debug=True)
