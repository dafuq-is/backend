import os
import requests
from sources.Exceptions import NoResultException

class Wordnik(object):
    def __init__(self):
        self._name = "wordnik"
        self._apiUrl = "http://api.wordnik.com/v4/word.json/"
        try:
            self._apiKey = os.environ['DAFUQ_IS_WORDNIK_API_KEY']
        except KeyError:
            self._apiKey = "default_api_key"

    def getMeaning(self, term):
        callUri = self._apiUrl + term + '/definitions?api_key=' + self._apiKey
        result = requests.get(callUri)
        answer = result.json()

        if not answer:
            raise NoResultException

        try:
            return answer[0]['text']
        except KeyError:
            raise NoResultException

    def getName(self):
        return self._name

