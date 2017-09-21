# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from recruit.utils import getDateStr


class UserItem(scrapy.Item):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['timestamp'] = getDateStr()

    positionId = scrapy.Field()
    positionName = scrapy.Field()
    userId = scrapy.Field()
    phone = scrapy.Field()
    portrait = scrapy.Field()
    receiveEmail = scrapy.Field()
    realName = scrapy.Field()
    userLevel = scrapy.Field()
    canTalk = scrapy.Field()
    timestamp = scrapy.Field()
    keyword = scrapy.Field()


class PositionItem(scrapy.Item):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['timestamp'] = getDateStr()

    positionId = scrapy.Field()
    positionName = scrapy.Field()
    companyId = scrapy.Field()
    companyLabelList = scrapy.Field()
    companyShortName = scrapy.Field()
    companyFullName = scrapy.Field()
    companyLogo = scrapy.Field()
    companySize = scrapy.Field()
    lastLogin = scrapy.Field()
    workYear = scrapy.Field()
    education = scrapy.Field()
    jobNature = scrapy.Field()
    financeStage = scrapy.Field()
    industryField = scrapy.Field()
    city = scrapy.Field()
    salary = scrapy.Field()
    positionAdvantage = scrapy.Field()
    district = scrapy.Field()
    createTime = scrapy.Field()
    approve = scrapy.Field()
    positionLables = scrapy.Field()
    industryLables = scrapy.Field()
    publisherId = scrapy.Field()
    businessZones = scrapy.Field()
    score = scrapy.Field()
    formatCreateTime = scrapy.Field()
    plus = scrapy.Field()
    pcShow = scrapy.Field()
    appShow = scrapy.Field()
    deliver = scrapy.Field()
    gradeDescription = scrapy.Field()
    promotionScoreExplain = scrapy.Field()
    firstType = scrapy.Field()
    secondType = scrapy.Field()
    isSchoolJob = scrapy.Field()
    imState = scrapy.Field()
    explain = scrapy.Field()
    adWord = scrapy.Field()
    timestamp = scrapy.Field()
    keyword = scrapy.Field()


    #           "companyId": 2380,
    #           "companyShortName": "浙江执御信息技术有限公司",
    #           "financeStage": "成长型(B轮)",
    #           "companyLogo": "i/image/M00/5E/25/Cgp3O1fqMFWAJ4hgAAAUycalP_8040.png",
    #           "companySize": "2000人以上",
    #           "companyLabelList": ["五险一金","带薪年假","节日礼物","年度旅游"],
    #           "publisherId": 6294718,
    #           "industryField": "移动互联网,数据服务",
    #           "industryLables": [],
    #           "companyFullName": "浙江执御信息技术有限公司",
    #           "positionId": 2819617,
    #           "positionAdvantage": "技术大牛,年终奖金,旅游活动,晋升空间",
    #           "positionName": "大数据运维",
    #           "workYear": "3-5年",
    #           "education": "不限",
    #           "jobNature": "全职",
    #           "salary": "15k-25k",
    #           "city": "杭州",
    #           "district": "拱墅区",
    #           "createTime": "2017-09-15 09:03:20",
    #           "approve": 1,
    #           "positionLables": ["资深","hadoop","数据库"],
    #           "lastLogin": 1505437387000,
    #           "score": 0,
    #           "businessZones": null,
    #           "formatCreateTime": "09:03发布",
    #           "plus": null,
    #           "pcShow": 0,
    #           "appShow": 0,
    #           "deliver": 0,
    #           "gradeDescription": null,
    #           "promotionScoreExplain": null,
    #           "firstType": "开发/测试/运维类",
    #           "secondType": "运维安全",
    #           "isSchoolJob": 0,
    #           "imState": "today",
    #           "explain": null,
    #           "adWord": 0
