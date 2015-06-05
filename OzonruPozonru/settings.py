# -*- coding: utf-8 -*-

# Scrapy settings for ozonru project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ozonru'

SPIDER_MODULES = ['ozonru.spiders']
NEWSPIDER_MODULE = 'ozonru.spiders'

USER_AGENT = 'Mozilla/5.0 (Ubuntu; X11; Linux x86_64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1 FirePHP/0.6'
ITEM_PIPELINES = ['ozonru.pipelines.OzonruPipeline']
CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 0.6

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ozonru (+http://www.yourdomain.com)'
