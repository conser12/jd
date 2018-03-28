# -*-coding:utf-8-*-
import json
import urllib

from bs4 import BeautifulSoup


class HtmlParser(object):
    def __init__(self):
        self.price_url = 'https://p.3.cn/prices/mgets?skuIds='

    def parser(self, page_url, html_contents):
        if html_contents is None:
            return

        soup = BeautifulSoup(html_contents, "html.parser", from_encoding='utf-8')
        new_data = self._get_data(page_url, soup)
        return new_data

    def _get_data(self, page_url, soup):

        res_data = {'url': page_url}

        title_code = soup.find('div', class_="sku-name")

        res_data['title'] = title_code.get_text().strip()

        price_node = soup.find('span', class_='p-price').find('span', class_='price')

        start_index = page_url.index(".com/") + 5

        price_id = "J_" + page_url[start_index: -5]
        url = self.price_url + price_id
        response = urllib.request.urlopen(url)

        if response.code == 200:
            response_content = response.read()
            price_json = bytes.decode(response_content)
            price_list = json.loads(price_json)
            if isinstance(price_list, list):
                price = price_list[0]['p']
                res_data['price'] = price

        return res_data
