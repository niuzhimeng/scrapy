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


class ScrapyDemoItem(scrapy.Item):
    # 封面
    cover = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 简述
    dec = scrapy.Field()
    # 播放地址
    playUrl = scrapy.Field()
