# Simple Backend for http://dafuq.is

Dafuq is a simple python script which calls [urbandictionary](https://www.urbandictionary.com/) API
for a given word and returns the response. The server is
written in python, using `bottle` and `requests`.


## Requirements

- `bottle` (Supplied with code, no need to install)
- `requests` v2.1.14
- `inotify-tools` (Install to OS)


## How to get up and running ?

- `$ pip install -r requirements.txt`
- `$ python ./src/index.py`

### For [Wordnik](https://www.wordnik.com/)

If you want to use wordnik source, you need to create an API key. 
After you have an API key do.

- `$ cp .env.example .env`
- Modify .env so that you paste your environment variable
- `$ source .env`
- `$ DAFUQ_IS_WORDNIK_API_KEY=${DAFUQ_IS_WORDNIK_API_KEY} python ./src/index.py`

**Note:** The app will run on localhost on port 8080,
we then setup our nginx proxy to forward requests 
from our web front to the app.

