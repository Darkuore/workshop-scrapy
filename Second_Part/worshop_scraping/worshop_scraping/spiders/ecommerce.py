import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['webscraper.io/test-sites/e-commerce/static']
    start_urls = ['http://webscraper.io/test-sites/e-commerce/static/']

    def parse(self, response):
        response = HtmlResponse(url='https://webscraper.io/test-sites/e-commerce/static', body=body)
        name = response.xpath('//title/text()').get()
        yield name
