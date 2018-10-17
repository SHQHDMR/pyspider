# -*- coding: utf-8 -*-
import scrapy
import bs4
import json
from pyspider.BdSpiderItems import BdspiderItem


class BdspiderSpider(scrapy.Spider):
    name = 'bdspider'
    allowed_domains = ['baidu.com']
    start_urls = [
        'http://baidu.com/s?w=1234',
    ]

    def parse(self, response):
        bs_soup = bs4.BeautifulSoup(response, features="lxml")
        div_c = bs_soup.find_all('div', class_='result c-container ')

        for div_obj in div_c:
            bd_spdier_item = BdspiderItem()
            bd_spdier_item['titile'] = div_obj.a.get_text()
            bd_spdier_item['abstract'] = div_obj.find('div', class_='c-abstract').get_text()
            bd_spdier_item['url_link'] = json.loads(div_obj.find('div', class_='c-tools')['data-tools'])['url']
            yield bd_spdier_item
