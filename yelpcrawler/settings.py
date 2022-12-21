BOT_NAME = 'yelpcrawler'

SPIDER_MODULES = ['yelpcrawler.spiders']
NEWSPIDER_MODULE = 'yelpcrawler.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 10
# The download delay setting will honor only one of:


# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
