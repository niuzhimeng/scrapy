# -*- coding: utf-8 -*-
import scrapy

from my_scrapy.items import MyScrapyItem

class JianshuSpider(scrapy.Spider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://www.jianshu.com/']

    def parse(self, response):
        for sel in response.xpath("//div[@class='content']"):
            torrent = MyScrapyItem()
            torrent['name'] = sel.xpath("a[@class='title']/text()").extract_first(default='not-found')
            torrent['description'] = sel.xpath("p[@class='abstract']/text()").extract_first().strip()
            torrent['href'] = 'http://www.jianshu.com' + sel.xpath("a[@class='title']/@href").extract_first()
            yield torrent
