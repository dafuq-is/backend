# Issues
- If its a request to add a new source, Use the `add-source` label.
- We currently do not have any Issue Templates. We will be figuring that out in future.

# Source Template

`src/sources/MyNewSource.py`
```python
class MyNewSource(WhatEverItExtends):
  def getName(self):
    return 'mySourceName'
    
  def getMeaning(term):
    term = doSomeConvolutedThing(term, 'stuffs')
    return term
```

