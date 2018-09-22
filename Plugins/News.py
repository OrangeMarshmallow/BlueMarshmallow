from Plugins.Base import BasePlugin as base
from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen


class NewsPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Новости'
        self.description = 'Отправляет последние новости'
        self.words = ["россия", "новость", "новости", "news", "russia"]

    def func(self):
        try:
            news_url = "https://news.google.ru/news/rss"
            client = urlopen(news_url)
            xml_page = client.read()
            client.close()

            soup_page = Soup(xml_page, "lxml")

            self.result['message'] = '\n\n'.join([n.title.text for n in soup_page.findAll("item")])
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
