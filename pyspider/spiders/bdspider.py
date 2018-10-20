# -*- coding: utf-8 -*-
import scrapy
import bs4
import json
from pyspider.BdSpiderItems import BdspiderItem


class BdspiderSpider(scrapy.Spider):
    name = 'bdspider'
    allowed_domains = ['baidu.com']
    start_urls = [
        'http://baidu.com/s?w=shqhdmr&pn=0',
    ]

    def parse(self, response):
        bs_soup = bs4.BeautifulSoup(response.text, features="lxml")
        div_c = bs_soup.find_all('div', class_='result c-container ')

        for div_obj in div_c:
            bd_spdier_item = BdspiderItem()
            bd_spdier_item['title'] = div_obj.a.get_text()
            bd_spdier_item['abstract'] = div_obj.find('div', class_='c-abstract').get_text()
            bd_spdier_item['url_link'] = json.loads(div_obj.find('div', class_='c-tools')['data-tools'])['url']
            yield bd_spdier_item
            print('-' * 20)
            print(bd_spdier_item['title'])
            print('-' * 20)
            print(bd_spdier_item['abstract'])
            print('-' * 20)
            print(bd_spdier_item['url_link'])
            print('-' * 20)

        print('?' * 50)
        print(self.allowed_domains[0] + bs_soup.find('a', class_='n')['href'])
        print('?' * 50)

        yield scrapy.Request("http://" + self.allowed_domains[0] + bs_soup.find('a', class_='n')['href'], self.parse)
