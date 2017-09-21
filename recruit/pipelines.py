# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymongo

from recruit.items import UserItem, PositionItem
from recruit.utils import getDateStr


class LagouPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    def open_spider(self, spider):
        dataStr = getDateStr()
        self.file_UserItem = open('data/UserItem-%s.json' % dataStr, 'w')
        self.file_PositionItem = open('data/PositionItem-%s.json' % dataStr, 'w')

    def close_spider(self, spider):
        self.file_UserItem.close()
        self.file_PositionItem.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        if isinstance(item, UserItem):
            self.file_UserItem.write(line)
        elif isinstance(item, PositionItem):
            self.file_PositionItem.write(line)
        return item


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', "mongodb://test:test@127.0.0.1:27017"),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'test')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # dic = dict(item)
        # dic = {}
        # dic["_id"] = item['positionId']
        # dic["$set"] = dict(item)

        self.db[item.__class__.__name__].update_one({"_id": item['positionId']}, {"$set": dict(item)}, True)
        return item
