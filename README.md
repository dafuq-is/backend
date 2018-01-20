# Simple Backend for http://dafuq.is

It a simple python script which calls urabndictionary api
for a given word and returns the response. The server is
written using `bottle` (dependency supplied with repo) and
`requests`.


## Requirements
- `bottle` (Supplied with code, no need to install)
- `requests` v2.1.14


## Running
- `$ pip install -r requirements.txt`
- `$ python ./src/index.py

Note: The app will run on localhost on port 8080,
we then setup our nginx proxy to forward requests 
from our web front to the app.
