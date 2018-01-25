from sources.UrbanDictionary import UrbanDictionary
from sources.Wordnik import Wordnik
from sources.Exceptions import SourceNotFound

_sourcesDict = {
    'ud': UrbanDictionary(),
    'wordnik': Wordnik()
}

def getSource(sourceName):
    if sourceName in _sourcesDict:
        return _sourcesDict[sourceName]

    raise SourceNotFound('The source ' + sourceName + ' was not found')

def getAllSources():
  return list(_sourcesDict.keys())

