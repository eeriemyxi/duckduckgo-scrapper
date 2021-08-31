from os import link
from ddg_scrapper import Async, search
import asyncio


"""Asynchronous"""

loop = asyncio.get_event_loop()
results = loop.run_until_complete(Async.search('myxi'))

"""Synchronous"""

results = search('myxi')


for result in results:
    list = [
        result.title,
        result.link,
        result.favicon,
        result.description
    ]
    json = result.json()
    print(list)
    print(json)