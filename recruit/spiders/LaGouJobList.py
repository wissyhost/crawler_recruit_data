# -*- coding: utf-8 -*-
import json
from urllib import parse

import math
import scrapy
import logging as log
import time

from lagou.items import UserItem, PositionItem
from lagou.settings import QUERY_KEYWORDS
from lagou.utils import ProgressBar


class LagouList(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    flag = 0
    keyword = QUERY_KEYWORDS[0]  # 默认第一个参数
    # city = "杭州"
    city = "全国"
    # city = "太原"
    pageSize = None
    pageNo = 0
    totalCount = None
    totalNum = 0
    fn = 0
    bar = None

    def parse(self, response):
        # print(response)
        # log.error(response.text)
        # print(response.text)
        try:
            data = json.loads(response.text)
            success = data['success']
            if success:
                self.fn = 0
                self.pageNo = data['content']['pageNo']
                if self.pageNo == 1:
                    self.totalCount = data['content']['positionResult']['totalCount']  # 从0开始循环
                    self.pageSize = data['content']['pageSize']
                    self.totalNum = math.ceil(self.totalCount / self.pageSize)
                    self.bar = ProgressBar(total=self.totalNum, keyword="%s/%s" % (self.keyword, self.city))
                    self.bar.log(
                        "=====>获取总页数 %s 页  <=====  %s%%" % (
                            self.totalNum, math.ceil((self.pageNo / self.totalNum) * 100)))
                    self.bar.log(
                        "=====>每页显示   %s 条  <=====  %s%%" % (
                            self.pageSize, math.ceil((self.pageNo / self.totalNum) * 100)))
                if self.totalCount and self.totalCount > 0:
                    for i in data['content']['hrInfoMap']:
                        ui = UserItem(data['content']['hrInfoMap'][i])
                        ui['positionId'] = i
                        ui['keyword'] = self.keyword
                        yield ui
                    for i in data['content']['positionResult']['result']:
                        pi = PositionItem(i)
                        pi['keyword'] = self.keyword
                        yield pi
                    yield self.getFromRequest(self.pageNo, self.totalNum, self.keyword, self.city, "false")
            else:
                self.fn += 1
                s = 20 + 5 * self.fn
                if self.pageNo + 1 > int(self.totalNum):
                    self.bar.log(
                        "=====>休眠 %s 秒        <=====  %s%%" % (s, math.ceil((self.pageNo / self.totalNum) * 100)))
                else:
                    self.bar.log(
                        "=====>休眠 %s 秒        <=====  %s%%" % (s, math.ceil((self.pageNo / self.totalNum) * 100)))

                time.sleep(s)
                if self.pageNo == 1:
                    yield self.getFromRequest(self.pageNo, self.totalNum, self.keyword, self.city, "true")
                else:
                    yield self.getFromRequest(self.pageNo, self.totalNum, self.keyword, self.city, "false")
            # 换关键词
            # log.info("换关键词1:%s" % self.pageNo)
            # log.info("换关键词2:%s" % self.totalNum)
            # log.info("换关键词3:%s" % (self.pageNo == self.totalNum))
            # log.info("换关键词4:%s" % (self.flag <= len(QUERY_KEYWORDS)))
            # log.info("关键词:" + QUERY_KEYWORDS[self.flag])
            if ((self.pageNo == self.totalNum) or (self.totalNum != 0 and self.pageNo == 0)) and (
                        self.flag < len(QUERY_KEYWORDS) - 2):
                self.flag = self.flag + 1
                self.keyword = QUERY_KEYWORDS[self.flag]
                yield self.getFromRequest(0, 2, self.keyword, self.city, "true")
        except Exception as e:
            log.error(response.text)
            print(e)
            raise e

    def start_requests(self):
        # FormRequest 是Scrapy发送POST请求的方法
        yield self.getFromRequest(0, 2, self.keyword, self.city, "true")

    def getFromRequest(self, currentPage, totalPage, keyword, city, first):
        # url = 'https://www.lagou.com/jobs/positionAjax.json?city=' + parse.unquote(
        #     city) + '&needAddtionalResult=false&isSchoolJob=0'
        url = 'https://www.lagou.com/jobs/positionAjax.json'
        page = currentPage + 1
        log.info(keyword + "\r")
        if page <= totalPage:
            if page != 1:
                self.bar.moveTo(page)
                self.bar.log("=====>正在抓取第 %s/%s 页<=====  %s%%" % (page, totalPage, math.ceil((page / totalPage) * 100)))
            # log.info("===>正在抓取第 %s/%s 页<===  %s%%" % (page, totalPage, math.ceil((page / totalPage) * 100)))
            # request=scrapy.Request(method="POST",url=url,body=b'kd=%E5%A4%A7%E6%95%B0%E6%8D%AE&first=true&pn=1',callback=self.parse,dont_filter=True)
            request = scrapy.FormRequest(url=url,
                                         formdata={'kd': keyword, 'pn': str(page), 'first': first, 'city': city,
                                                   'needAddtionalResult': 'false', 'isSchoolJob': '0'},
                                         callback=self.parse, dont_filter=True)
            request.headers.appendlist("Referer", "https://www.lagou.com/jobs/list_" + parse.unquote(
                keyword) + "?labelWords=&fromSearch=true&suginput=")
            return request
        else:
            log.info("抓取完毕")
