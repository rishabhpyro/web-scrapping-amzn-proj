import scrapy
from ..items import AmznprojItem
import pandas as pd


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = [
        'https://www.amazon.com/threat-andrew-mccabe/s?k=the+threat+andrew+mccabe&qid=1606066091&ref=sr_pg_1'
    ]

    def parse(self, response):

        items = AmznprojItem()

        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.sg-col-12-of-28 .a-size-base+ .a-size-base').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()


        items['product_name'] = product_name
        items['product_author'] = self.update_func(product_author)
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

    def update_func(self,dummy):
        k=[]
        for i in dummy:
            j= i.replace('\n','').strip()
            k.append(j)

        return k

