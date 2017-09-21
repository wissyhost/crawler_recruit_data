# -*- coding: utf-8 -*-

# Scrapy settings for recruit project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'recruit'
IPPOOL_FILE = "recruit/ippool.json"
IPPOOL_FLUSH_TIME = 20  # s
IPPOOL_FLUSH_FILE_MINUTE = 60  # m
SPIDER_MODULES = ['recruit.spiders']
NEWSPIDER_MODULE = 'recruit.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'recruit (+http://www.yourdomain.com)'
# USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = True
LOG_LEVEL = "ERROR"
# LOG_LEVEL = "INFO"
# LOG_LEVEL = "DEBUG"

# QUERY_KEYWORDS = ["大数据", "Spark", "Hadoop", "算法", "工程师"]
# QUERY_KEYWORDS = ["工程师"]
QUERY_KEYWORDS = ["WEB", "前端", "后端"]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
DOWNLOAD_TIMEOUT = 5
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #   'Accept-Language': 'en',
    'Cookie': 'JSESSIONID=ABAAABAACEBACDG61C29EB6A82004722F726AA83A90C0EE;_ga=GA1.2.1725904311.1505640456;_gid=GA1.2.481084446.1505640456;Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1505640456,1505640921;Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1505640970;user_trace_token=20170917172736-71080dbb-9b8a-11e7-95bd-525400f775ce;LGSID=20170917172736-71081167-9b8a-11e7-95bd-525400f775ce;PRE_UTM=m_cf_cpt_baidu_pc;PRE_HOST=bzclk.baidu.com;PRE_SITE=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00f7Ghk60yUKm0FNkUsjB5o4u00000PW4pNb00000UtUWJM.THL0oUhY1x60UWdBmy-bIfK15H-hujw9nvDYnj0snynkryR0IHYdnWRvfWcdfYnYwbR1PWfkwj7jPj7jwHnvPRuKrjK7n6K95gTqFhdWpyfqn101n1csPHnsPausThqbpyfqnHm0uHdCIZwsT1CEQLILIz4_myIEIi4WUvYE5LNYUNq1ULNzmvRqUNqWu-qWTZwxmh7GuZNxTAn0mLFW5HndnjDs%26tpl%3Dtpl_10085_15730_11224%26l%3D1500117464%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591%2525E5%2525AE%252598%2525E7%2525BD%252591-%2525E4%2525B8%252593%2525E6%2525B3%2525A8%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E8%252581%25258C%2525E4%2525B8%25259A%2525E6%25259C%2525BA%2526xp%253Did%28%252522m6c247d9c%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D220%26ie%3Dutf-8%26f%3D3%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rqlang%3Dcn%26inputT%3D2294%26prefixsug%3Dlagou%26rsp%3D0;PRE_LAND=https%3A%2F%2Fwww.recruit.com%2F%3Futm_source%3Dm_cf_cpt_baidu_pc;LGRID=20170917173610-a3682b5e-9b8b-11e7-95be-525400f775ce;LGUID=20170917172736-71081433-9b8a-11e7-95bd-525400f775ce;X_HTTP_TOKEN=3271eb30778134979e92198258250b78;ab_test_random_num=0;_putrc=0E441BE34E241012;login=true;unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B78002;hasDeliver=0;_gat=1;showExpriedIndex=1;showExpriedCompanyHome=1;showExpriedMyPublish=1;index_location_city=%E5%85%A8%E5%9B%BD;TG-TRACK-CODE=search_code;SEARCH_ID=5cfefacb864943109662fed5ee1fc35e',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'recruit.middlewares.LagouSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #    'recruit.middlewares.MyCustomDownloaderMiddleware': 543,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 543,
    #     'recruit.middlewares.MyproxiesSpiderMiddleware': 125,
    #     'recruit.middlewares.ProxyMiddleware': 542,
    #     'recruit.middlewares.CatMiddleware': 999,
}
# HTTPPROXY_ENABLED=True

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'recruit.pipelines.LagouPipeline': 300,
    'recruit.pipelines.JsonWriterPipeline': 300,
    'recruit.pipelines.MongoPipeline': 300,
}


# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
