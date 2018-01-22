from sources.UrbanDictionary import UrbanDictionary
from sources.Wordnik import Wordnik

_sourcesDict = {
    'ud': UrbanDictionary(),
    'wordnik': Wordnik()
}

def getSource(sourceName):
    return _sourcesDict[sourceName]

def getAllSources():
  return _sourcesDict.keys()

