##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## item
##

from matplotlib.style import available
import scrapy

class Product(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    id = scrapy.Field()
    current_url = scrapy.Field()
    image = scrapy.Field()
    detail_link = scrapy.Field()
    price = scrapy.Field()
    old_price = scrapy.Field()
    available = scrapy.Field()
    flag = scrapy.Field()




