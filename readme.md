### Asynchronous and synchronous Duckduckgo.com search engine scrapper

#### Asynchronous
```python
from ddgscrapper import Async
import asyncio

loop = asyncio.get_event_loop()
results = loop.run_until_complete(Async.search('myxi'))
```
#### Synchronous
```python
from ddgscrapper import search

results = search('myxi')
```

#### Return value
it returns a list of [**`DDG`**](https://github.com/m-y-x-i/duckduckgo-scrapper/blob/9a257ad4d92defe606e3d6b7321904d2d18e8b35/ddg_scrapper.py#L7-L16) object. 


Attributes:
 - title
 - link
 - favicon
 - description

Methods:
 - `json()`
returns python dictionary object with the attributes of DDG as keys.

Check [**`how-to.py`**](https://github.com/m-y-x-i/duckduckgo-scrapper/blob/main/how-to.py#L16-L25) for more information.
