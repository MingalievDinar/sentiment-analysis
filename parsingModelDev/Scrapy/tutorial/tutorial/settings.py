# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

#BOT_NAME = 'tutorial'
BOT_NAME = 'tutorial2'
CONCURRENT_ITEMS = 32
CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 32
DOWNLOAD_DELAY = 100
SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
DOWNLOAD_TIMEOUT = 100

#CLOSESPIDER_ERRORCOUNT = 0
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36' 

DEFAULT_REQUEST_HEADERS = {
	"Accept-Encoding":"gzip, deflate, sdch",
	"Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4"
	}

HTTPCACHE_ENABLED = False   # Turns off disk cache, which has low hit ratio during broad crawls
REDIRECT_ENABLED = False
COOKIES_ENABLED = True
RETRY_ENABLED = False   # Retries can be handled by Frontera itself, depending on crawling strategy
DOWNLOAD_MAXSIZE = 10 * 1024 * 1024  # Maximum document size, causes OOM kills if not set
LOGSTATS_INTERVAL = 10  # Print stats every 10 secs to console


#DOWNLOADER_MIDDLEWARES = {'scrapy_crawlera.CrawleraMiddleware': 300}
#CRAWLERA_ENABLED = True
#CRAWLERA_APIKEY = '39768b97f09244a9994509d17defe018'
#CRAWLERA_PRESERVE_DELAY = 500



AUTOTHROTTLE_ENABLED = True
RANDOMIZE_DOWNLOAD_DELAY = True
AUTOTHROTTLE_TARGET_CONCURRENCY = 2
AUTOTHROTTLE_START_DELAY = 2
AUTOTHROTTLE_MAX_DELAY = 60


#RANDOMIZE_DOWNLOAD_DELAY = False



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tutorial.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
