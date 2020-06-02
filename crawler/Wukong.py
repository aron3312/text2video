from lxml import etree
import requests

class WukongCrawler(object):
    def __init__(self):
        self.url = "https://www.wukong.com/"