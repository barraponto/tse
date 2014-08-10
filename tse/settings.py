# -*- coding: utf-8 -*-
import os.path


BOT_NAME = 'tse'
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

SPIDER_MODULES = ['tse.spiders']
NEWSPIDER_MODULE = 'tse.spiders'
ITEM_PIPELINES = {'tse.pipelines.StatePipeline'}
FILES_STORE = os.path.join(PROJECT_ROOT, 'files')

FEED_URI = os.path.join(PROJECT_ROOT, 'results.json')
FEED_FORMAT = 'json'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tse (+http://www.yourdomain.com)'
