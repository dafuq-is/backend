#!/usr/bin/env python3

from bottle import route, run, HTTPResponse
from sources.Exceptions import NoResultException
from sources import Factory

@route('/<word>')
@route('/<word>/<service>')
def choose(word, service='ud'):
    try:
        meaning = Factory.getSource(service).getMeaning(word)
    except NoResultException:
        return HTTPResponse(status=404, body="Dafuq! <b>" + service + "</b> does not know about <b>" + word + "</b>! ")
    except KeyError:
        supported = ", ".join(Factory.getAllSources())
        return HTTPResponse(status=404, body="Dafuq! <b>" + service + "</b> is not supported. Use: <i>" + supported + "</i>!")


    return HTTPResponse(status=200, body=meaning)


run(host='0.0.0.0', port=8080, debug=True)
