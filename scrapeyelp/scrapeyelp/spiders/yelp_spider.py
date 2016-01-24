# Abhishek Gupta (ag4cb@virginia.edu)

import scrapy
from scrapeyelp.items import Restaurant

class YelpSpider(scrapy.Spider):

    name = "yelp"
    allowed_domains = ["yelp.com"]
    start_urls = [
        "http://www.yelp.com/search?cflt=restaurants&find_loc=Charlottesville%2C+VA%2C+USA"
    ]
    def __init__(self):
        self.count= 0

    def parse(self, response):
        for listing in response.xpath('//li[@class="regular-search-result"]/div/div/div[@class="main-attributes"]'):
            item = Restaurant()
            item["name"] = listing.xpath('.//a[@class="biz-name"]/span/text()').extract_first().encode('ascii', 'ignore')
            item["rating"] = float(listing.xpath('.//div[@class="rating-large"]/i/@title').extract_first().split()[0])
            choices = ["Inexpensive", "Moderate", "Pricey", "Ultra High-End"]
            pricestr = listing.xpath('.//span[@class="business-attribute price-range"]/text()').extract_first()
            item["price"] = choices[pricestr.count('$')-1] if type(pricestr)==unicode else "n/a"
            item["categories"] = [str(i) for i in listing.xpath('.//span[@class="category-str-list"]/a/text()').extract()]
            self.count+=1
            yield item
        if self.count < 100:
            rel_url = response.xpath('//a[@class="page-option prev-next next"]/@href').extract_first()[:-2]
            next_page = response.urljoin(rel_url+str(self.count))
            yield scrapy.Request(next_page, self.parse)
            
