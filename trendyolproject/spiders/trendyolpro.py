#Selenium imports here
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time



driver = webdriver.Chrome(executable_path=r'C:/Web_driver_for_selenium/chromedriver.exe')

driver.get('https://www.trendyol.com/')

kabul_et =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))).click()

arama =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Aradığınız ürün, kategori veya markayı yazınız"]')))
arama.clear()
anahtarkelime = input('Lütfen aramak istediğiniz öğeyi yazınız: ')
arama.send_keys(anahtarkelime)
arama.send_keys(Keys.ENTER)

current_link = str(driver.current_url)



import scrapy
from ..items import TrendyolprojectItem

class Trendyolspider(scrapy.Spider):
    name = "trendy"
    start_urls = [
        current_link
    ]

    def parse(self, response):
        items = TrendyolprojectItem()
        all_data_pc = response.css('div.p-card-wrppr')
        for trendy in all_data_pc:

            price = trendy.css('div.prc-box-dscntd::text').get()
            brand = trendy.css('span.prdct-desc-cntnr-ttl::text').get()
            features = trendy.css('span.prdct-desc-cntnr-name.hasRatings::text').get()

            items['price'] = price
            items['brand'] = brand
            items['features'] = features

            yield items


