# -*- coding: utf-8 -*-
import scrapy


class StateItem(scrapy.Item):
    state = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()

class ZoneItem(scrapy.Item):
    state = scrapy.Field()
    number = scrapy.Field()
    code = scrapy.Field()
    address = scrapy.Field()
    cep = scrapy.Field()
    neighborhood = scrapy.Field()
    city = scrapy.Field()
