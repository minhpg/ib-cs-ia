import requests
from bs4 import BeautifulSoup 

class BeautifulSoup:
    def __init__(url,proxies=None,headers=None):
        self.url = url
        self.proxies = proxies
        self.headers = headers
        self.source = self.getSource()

    def getSource(self):
        response = requests.get(
            url = url,
            proxies = proxies,
            headers = headers
        )
        return BeautifulSoup(response.text,'html.parser')



from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class Scrapy:
    def __init__()