import requests
#import NotFoundException

class UrbanDictionary(object):
    def __init__(self):
        self._name = 'Urban Dictionary'
        self._apiBaseUrl = 'http://api.urbandictionary.com/v0/define?term='

    def getMeaning(self, term):
        callUrl = self._apiBaseUrl + term
        result = requests.get(callUrl)
        try:
            answer = result.json()
        except ValueError:
            # @todo: log this in future
            raise NotFoundException('We could not find the term')
        if not answer["list"]:
            raise  NotFoundException('We could not find the term')
       
        return answer["list"][0]["definition"]


