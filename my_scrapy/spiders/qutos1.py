# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # follow links to author pages
        for href in response.xpath("//div[@class='quote']//a[1]/@href").extract():
            yield scrapy.Request(response.urljoin(href), callback=self.parse_author)

        # follow pagination links
        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.xpath(query).extract_first().strip()

        yield {
            'name': extract_with_css("//h3[@class='author-title']/text()"),
            'birthday': extract_with_css("//span[@class='author-born-date']/text()"),
            'birthplace': extract_with_css("//span[@class='author-born-location']/text()"),
            'bio': extract_with_css("//div[@class='author-description']/text()"),
        }
