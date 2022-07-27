# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TrendyolItem(scrapy.Item):

    Marka = scrapy.Field()
    İşlemci = scrapy.Field()
    SSD = scrapy.Field()
    EkranKartı = scrapy.Field()
