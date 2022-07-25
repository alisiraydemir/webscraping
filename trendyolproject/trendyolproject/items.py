# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TrendyolprojectItem(scrapy.Item):
    price = scrapy.Field()
    brand = scrapy.Field()
    features = scrapy.Field()

