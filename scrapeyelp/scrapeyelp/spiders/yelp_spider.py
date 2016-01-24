import scrapy
from scrapeyelp.items import Restaurant

class YelpSpider(scrapy.Spider):

    name = "yelp"
    allowed_domains = ["yelp.com"]
    start_urls = [
        "http://www.yelp.com/search?cflt=restaurants&find_loc=Charlottesville%2C+VA%2C+USA"
    ]
    count = 0

    def parse(self, response):
        count+=1
        for blah in blah:
            item = Restaurant()
            item["name"] = blah
            item["rating"] = blah
            item["price"] = blah
            item["categories"] = blah
            yield item
        if count<10:
            next_page = blah
            yield scrapy.Request(next_page, self.parse)
            
