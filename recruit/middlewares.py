# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import json
import time
import logging as log

import math
from scrapy import signals
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware


class LagouSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


import random
from scrapy import signals
from recruit.settings import IPPOOL_FILE, IPPOOL_FLUSH_TIME


class MyproxiesSpiderMiddleware(object):
    def __init__(self, ip=''):
        self.ip = ip
        self.IPPOOL = None
        self.flushIpDate = 0
        log.info("初始化代理")
        # todo 定时
        self.flushIpPool()

    def flushIpPool(self):
        # print(int(time.time()))
        if self.IPPOOL or self.flushIpDate == 0 or int(time.time()) - self.flushIpDate > IPPOOL_FLUSH_TIME:
            self.loadIPPOOL()

    def loadIPPOOL(self):
        with open(IPPOOL_FILE) as f:
            json_load = json.load(f)
            if json_load.keys().__contains__("proxys"):
                ips = json_load['proxys']
                if ips and len(ips) > 0:
                    self.IPPOOL = ips
                    self.flushIpDate = int(time.time())

    def process_request(self, request, spider):
        log.info("使用代理")
        # print(self.IPPOOL)
        if self.IPPOOL:
            thisip = random.choice(self.IPPOOL)
            print("this is ip %s" % thisip)
            request.meta["proxy"] = thisip
            protocol = 'https' if 'https' in thisip else 'http'
            request.meta["proxies"] = {protocol: thisip}


# # -*- coding: utf-8 -*-
# class ProxyMiddleware(object):
#     proxys = ["183.56.177.130:808", "119.57.112.181:8080", "122.200.84.13:8080", "101.200.82.141:8888"]
#
#     def process_request(self, request, spider):
#         if request.url.startswith("https://"):
#             request.meta['proxy'] = "https://%s" % random.choice(self.proxys)
#         elif request.url.startswith("http://"):
#             request.meta['proxy'] = "http://%s" % random.choice(self.proxys)
#
#
# from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

import base64


# proxyServer = "http://proxy.abuyun.com:9020"

# 代理隧道验证信息
# proxyUser = "H15R7916E964W3BD"
# proxyPass = "3BB2230E001B234D"

# proxyHost = "proxy.abuyun.com"
# proxyPort = "9020"
# 代理隧道验证信息
# proxyUser = "HN9CB8L4K2GT4O5D"
# proxyPass = "CA6472538A31E64B"

# 代理服务器
# proxyServer = "http://http-dyn.abuyun.com:9020"

# 代理隧道验证信息
# proxyUser = "H01234567890123D"
# proxyPass = "0123456789012345"

# for Python2
# proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)


# for Python3
# proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

# class ProxyMiddleware(object):
#     def process_request(self, request, spider):
#         log.info("使用代理")
#         request.meta["proxy"] = proxyServer
#         request.headers["Proxy-Authorization"] = proxyAuth


# class ProxyMiddleware(object):
#     def process_request(self, request, spider):
#         log.info("使用代理")
#         request.meta["proxy"] = proxyServer
#         request.headers["Proxy-Authorization"] = proxyAuth
class CatMiddleware(object):
    def process_request(self, request, spider):
        log.info(request.headers)
        # request.meta["proxy"] = proxyServer
        # request.headers["Proxy-Authorization"] = proxyAuth
