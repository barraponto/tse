# -*- coding: utf-8 -*-

# Scrapy settings for tse project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tse'

SPIDER_MODULES = ['tse.spiders']
NEWSPIDER_MODULE = 'tse.spiders'
ITEM_PIPELINES = {'tse.pipelines.StatePipeline'}
FILES_STORE = 'files'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tse (+http://www.yourdomain.com)'
