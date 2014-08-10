# -*- coding: utf-8 -*-
from urlparse import urljoin
import scrapy
from ..items import StateItem

class ZonesSpider(scrapy.Spider):
    name = "zones"
    allowed_domains = ["estatistica.tse.jus.br"]
    start_urls = (
        'http://estatistica.tse.jus.br:7777/dwtse/f?p=600:',
    )

    def parse(self, response):
        # Just getting cookies the first time around.
        return (scrapy.Request(self.start_urls[0] + str(n), self.parse_state)
                for n in xrange(1, 29))

    def parse_state(self, response):
        item = StateItem()
        item['state'] = response.css(
            '.t15RegionHeader::text').extract()[0].split('-')[-1].strip()
        item['file_urls'] = [urljoin(
            response.url,
            response.css('span.left a::attr(href)').extract()[0])]
        return item
