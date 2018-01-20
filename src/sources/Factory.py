from sources.UrbanDictionary import UrbanDictionary
from sources.Wordnik import Wordnik

class Factory(object):
    def __init__(self):
        self._sourceDicts = {
            'ud': UrbanDictionary(),
            'wordnik': Wordnik()
        }

    def getSource(self, sourceName):
        return self._sourceDicts[sourceName]

    def getAllSources(self):
        return self._sourceDicts.keys()

