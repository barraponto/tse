# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
# from scrapy.shell import inspect_response


class SectionsSpider(scrapy.Spider):
    name = "sections"
    allowed_domains = ["chimera.tse.jus.br"]
    start_urls = (
        'http://chimera.tse.jus.br:7777/eletse/apex/f?p=20121:1:2493722937624290',
    )

    def parse(self, response):
        return FormRequest.from_response(
            response, formdata={'p_t01': '1'},
            callback=self.parse_states, dont_filter=True)

    def parse_states(self, response):
        for state in response.css('[name=p_t02] option::attr(value)').extract()[1:]:
            response.meta.update({'state': state})
            yield FormRequest.from_response(response, meta=response.meta, formdata={
                'p_t01': '1',
                'p_t02': state
            }, callback=self.parse_cities, dont_filter=True)

    def parse_cities(self, response):
        for city in response.css('[name=p_t03] option::attr(value)').extract()[1:]:
            response.meta.update({'city': city})
            yield FormRequest.from_response(response, meta=response.meta, formdata={
                'p_t01': '1',
                'p_t02': response.meta['state'],
                'p_t03': city
            }, callback=self.parse_zones, dont_filter=True)

    def parse_zones(self, response):
        for zone in response.css('[name=p_t04] option::attr(value)').extract()[1:]:
            response.meta.update({'zone': zone})
            yield FormRequest.from_response(response, meta=response.meta, formdata={
                'p_t01': '1',
                'p_t02': response.meta['state'],
                'p_t03': response.meta['city'],
                'p_t04': zone
            }, callback=self.parse_sections, dont_filter=True)

    def parse_sections(self, response):
        for section in response.css('[name=p_t05] option::attr(value)').extract()[1:]:
            response.meta.update({'section': section})
            yield FormRequest.from_response(response, meta=response.meta, formdata={
                'p_t01': '1',
                'p_t02': response.meta['state'],
                'p_t03': response.meta['city'],
                'p_t04': response.meta['zone'],
                'p_t05': section,
                'p_request': 'PESQUISAR'
            }, callback=self.parse_section, dont_filter=True)

    def parse_section(self, response):
        # inspect_response(response)
        pass
