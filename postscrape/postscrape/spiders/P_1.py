import scrapy 
from scrapy import Request
import re

class PostsSpider(scrapy.Spider):
    name = "posts"
    start_urls = ['https://www.kijiji.ca/b-cars-trucks/ontario/honda__mazda__subaru__toyota__volkswagen-new__used/c174l9004a54a49?transmission=1']
    allowed_domains  = ['kijiji.ca']

    def parse(self, response):
        blocks = response.css('div.info-container')

        for block in blocks:
           partial_url =  "https://www.kijiji.ca" + str((block.css('a.title::attr(href)').extract())[0])
           
           yield Request(partial_url, callback = self.page_informarion)
    
        next_partial_url = "https://www.kijiji.ca" + str((response.css('div.bottom-bar').css('a[title="Next"]::attr(href)').extract())[0])
        
        yield Request(next_partial_url, callback = self.parse)
    
    def page_informarion(self, response):

        yield{
            'url' : response.url,
            'Price' : (response.css('span[itemprop="price"]::text')).extract()[0],
            'Brand' : (response.css('dd[itemprop="brand"]').css('a::text')).extract()[0],
            'Model' : (response.css('dd[itemprop="model"]').css('a::text')).extract()[0]
        }
    def additional_information(self, response):

        



  
        