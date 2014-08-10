# -*- coding: utf-8 -*-
from urlparse import urljoin
import scrapy
from ..items import StateItem, ZoneItem

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
        state = StateItem()
        state['state'] = response.css(
            '.t15RegionHeader::text').extract()[0].split('-')[-1].strip()
        state['file_urls'] = [urljoin(
            response.url,
            response.css('span.left a::attr(href)').extract()[0])]

        yield state

        for row in response.css('div[id] tr')[1:-1]:
            zone = ZoneItem()
            zone['state'] = state['state']
            zone['number'] = row.xpath('./td[1]/text()').extract()[0]
            zone['code'] = row.xpath('./td[2]/text()').extract()[0]
            zone['address'] = row.xpath('./td[3]/text()').extract()[0]
            zone['cep'] = row.xpath('./td[4]/text()').extract()[0]
            zone['neighborhood'] = row.xpath('./td[5]/text()').extract()[0]
            zone['city'] = row.xpath('./td[6]/text()').extract()[0]
            yield zone
