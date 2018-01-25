import os
import requests
from sources.Exceptions import NoResultException

class Wordnik(object):
    def __init__(self):
        self._name = "wordnik"
        self._apiUrl = "http://api.wordnik.com/v4/word.json/"
        self._apiKey = os.environ['DAFUQ_IS_WORDNIK_API_KEY']

    def getMeaning(self, term):
        callUri = self._apiUrl + term + '/definitions?api_key=' + self._apiKey
        result = requests.get(callUri)
        answer = result.json()

        if not answer:
            raise NoResultException

        return answer[0]['text']

    def getName(self):
        return self._name

