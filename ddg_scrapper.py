import aiohttp
import requests
import furl
from bs4 import BeautifulSoup as bs4


class DDG:
    def __init__(self, dict) -> dict:
        self._dict = dict
        self.title = dict["title"]
        self.link = dict["link"]
        self.description = dict["description"]
        self.favicon = dict["favicon"]

    def json(self):
        return self._dict


class Async:
    async def search(keyword: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://html.duckduckgo.com/html/?q={keyword}"
            ) as response:
                content = await response.text()
                parser = bs4(content, "html.parser")
                links = parser.find("div", attrs={"id": "links"})
                results = links.find_all(
                    "div",
                    attrs={
                        "class": "result results_links results_links_deep web-result"
                    },
                )
                final = []
                for result in results:
                    title = result.find(
                        "h2", attrs={"class": "result__title"}
                    ).text.strip("\n")
                    link = (
                        "https:"
                        + result.find("a", attrs={"class": "result__url"}, href=True)[
                            "href"
                        ]
                    )
                    link = furl.furl(link).args["uddg"]
                    description = result.find(
                        "a", attrs={"class": "result__snippet"}
                    ).text
                    favicon = (
                        "https:"
                        + result.find("img", attrs={"class": "result__icon__img"})[
                            "src"
                        ]
                    )
                    final.append(
                        DDG(
                            {
                                "title": title,
                                "link": link,
                                "favicon": favicon,
                                "description": description,
                            }
                        )
                    )
                return final


def search(keyword: str):
    content = requests.get(
        f"https://html.duckduckgo.com/html/?q={keyword}",
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
        },
    ).text
    parser = bs4(content, "html.parser")
    links = parser.find(attrs={"id": "links"})
    results = links.find_all(
        "div",
        attrs={"class": "result results_links results_links_deep web-result"},
    )
    final = []
    for result in results:
        title = result.find("h2", attrs={"class": "result__title"}).text.strip("\n")
        link = result.find("a", attrs={"class": "result__url"}, href=True)["href"]
        description = result.find("a", attrs={"class": "result__snippet"}).text
        favicon = (
            "https:" + result.find("img", attrs={"class": "result__icon__img"})["src"]
        )
        final.append(
            DDG(
                {
                    "title": title,
                    "link": link,
                    "favicon": favicon,
                    "description": description,
                }
            )
        )
    return final
