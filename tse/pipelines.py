# -*- coding: utf-8 -*-
from os.path import dirname, join
from scrapy.contrib.pipeline.files import FilesPipeline
from scrapy.http import Request


class StatePipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, meta={'item': item}) for x in item.get(self.FILES_URLS_FIELD, [])]
    def file_path(self, request, response=None, info=None):
        path = super(StatePipeline, self).file_path(request, response, info)
        return join(dirname(path), request.meta['item']['state'] + '.xls')
