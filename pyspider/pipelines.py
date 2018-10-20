# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PyspiderPipeline(object):
    def process_item(self, item, spider):
        item['title'] = '标题：' + item['title']
        item['abstract'] = '摘要：' + item['abstract']
        item['url_link'] = '链接：' + item['url_link']
        return item
