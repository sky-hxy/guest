'''
Author: hxy 1305149167@qq.com
Date: 2023-05-09 00:41:56
LastEditors: hxy 1305149167@qq.com
LastEditTime: 2023-05-09 01:13:52
FilePath: /Python-100-Days-master/demoapi/demoapi/pipelines.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl
from demoapi.items import DoubanItem

class DemoapiPipeline:

    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.title = 'Top250'
        self.sheet.append(('名称', '评分', '名言'))

    def process_item(self, item: MovieItem, spider):
        self.sheet.append((item['title'], item['score'], item['motto']))
        return item

    def close_spider(self, spider):
        self.wb.save('豆瓣电影数据.xlsx')