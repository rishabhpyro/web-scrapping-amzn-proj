import scrapy


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
