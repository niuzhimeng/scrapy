# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyScrapyItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    href = scrapy.Field()


class jian_shu(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    href = scrapy.Field()
