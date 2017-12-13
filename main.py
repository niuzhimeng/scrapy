from scrapy import cmdline

cmdline.execute('scrapy crawl movie -o nzm.json'.split())
