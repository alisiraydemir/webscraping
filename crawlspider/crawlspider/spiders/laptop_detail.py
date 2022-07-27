import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TrendyolItem

class LaptopCrawlSpider(CrawlSpider):
    name = 'laptop_crawl'
    allowed_domains = ['trendyol.com']
    start_urls = ['https://www.trendyol.com/sr?q=laptop&qt=laptop&st=laptop&os=1']

    laptop_detail_link_rules  = LinkExtractor(restrict_xpaths='//div[@class="prdct-cntnr-wrppr"]')
    laptop_detail = Rule(laptop_detail_link_rules,
                         callback='parse_item',
                         follow=False)
    rules = (
        laptop_detail,
    )

    def parse_item(self, response):
        items = TrendyolItem()
        all_data_pc = response.css('section.details-section')

        for info in all_data_pc:
            Marka = info.css('.detail-name::text').getall()
            İşlemci = info.css('.detail-attr-item:nth-child(1) b::text').get()
            SSD   = info.css('.detail-attr-item:nth-child(2) b::text').get()
            EkranKartı = info.css('.detail-attr-item:nth-child(4) b::text').get().replace('Ev - Okul', '').replace('Ofis - İş', '')

            items['Marka'] = Marka
            items['İşlemci'] = İşlemci
            items['SSD'] = SSD
            items['EkranKartı'] = EkranKartı

            yield items

"""import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('crawlspider/laptop.csv')
df.head(25)"""