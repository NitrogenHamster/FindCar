import scrapy 
import re

class Post1Spider(scrapy.Spider):
    name = "post_1"

    start_urls ={'https://www.kijiji.ca/b-cars-trucks/ontario/new__used/c174l9004a49'}

    def parse(self, response):
        yield{
            'url': 'y'
            #'nunber': response.css('div.showing::text').get()
            }

        