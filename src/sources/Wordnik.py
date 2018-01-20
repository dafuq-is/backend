from wordnik import swagger, WordApi

class Wordnik(object):
    def __init__(self):
        self._name = 'wordnik'
        self._apiUrl = 'http://api.wordnik.com/v4'
        self._apiKey = 'MY_API_KEY'
        self._client = swagger.ApiClient(self._apiUrl, self._apiKey)

    def getMeaning(self, term):
        wordApi = WordApi.WordApi(self._client)
        definition = wordApi.getDefinitions(term)
        return definition[0].text

