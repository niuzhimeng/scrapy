# -*- coding: utf-8 -*-
import scrapy

from my_scrapy.items import ScrapyDemoItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['vmovier.com']
    start_urls = ['http://www.vmovier.com/']

    def parse(self, response):
        moivelist = response.xpath("//li[@class='clearfix']")

        for m in moivelist:
            item = ScrapyDemoItem()
            item['cover'] = m.xpath('./a/img/@src')[0].extract()
            item['title'] = m.xpath('./a/@title')[0].extract()
            item['dec'] = m.xpath("./div/div[@class='index-intro']/a/text()")[0].extract()
            # print(item)

            # 提取电影详细页面 url 地址
            urlitem = m.xpath('./a/@href').extract_first()
            url = response.urljoin(urlitem)
            # 如果你想将上面的 item 字段传递给 parse_moive, 使用 meta 参数
            yield scrapy.Request(url, callback=self.parse_moive, meta={'item': item})

    def parse_moive(self, response):
        it = response.meta['item']
        item = ScrapyDemoItem()
        item['cover'] = it['cover']
        item['title'] = it['title']
        item['dec'] = it['dec']
        item['playUrl'] = response.xpath("//div[@class='p00b204e980']/p/iframe/@src")[0].extract()
        print('=======================')
        yield item
