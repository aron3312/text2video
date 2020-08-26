from lxml import etree
import requests
import json
import urllib.parse


class WukongCrawler(object):
    def __init__(self):
        self.url = "https://www.wukong.com/wenda/web/search/brow/?search_text={q}&offset={offset}&count=10&_signature=eqkurgAgEBJ7R-AdP0esNnqpLrAACR."

    def get_search_result(self, q):
        req = requests.get(self.url.format(q=q, offset=''), headers={
                     "referer": "https://www.wukong.com/search/?keyword={}".format(urllib.parse.quote(q)),
                     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"})
        question_data = json.loads(req.content)
        print(question_data['data']['feed_question'])

if __name__ == '__main__':
    a = WukongCrawler()
    a.get_search_result("外星人")