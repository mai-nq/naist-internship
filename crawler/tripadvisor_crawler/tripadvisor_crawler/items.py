# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class PostItem(scrapy.Item):
    post_date = scrapy.Field()
    post_body = scrapy.Field()
