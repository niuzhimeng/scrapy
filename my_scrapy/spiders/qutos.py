# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com',
    ]
    allowed_domains = [
        'toscrape.com',
    ]

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'quote': quote.xpath("span[@class='text']/text()").extract_first().strip(),
                'author': quote.xpath("//small[@class='author']/text()").extract_first().strip(),
                'tags': quote.xpath("div[@class='tags']//a/text()").extract(),
            }

        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        print('url====' + next_page)
        next_full_url = response.urljoin(next_page)
        print('============================' + next_full_url)
        yield scrapy.Request(next_full_url, callback=self.parse)
