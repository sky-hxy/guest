'''
Author: hxy 1305149167@qq.com
Date: 2023-05-09 00:41:56
LastEditors: hxy 1305149167@qq.com
LastEditTime: 2023-05-09 00:46:09
FilePath: /Python-100-Days-master/demoapi/demoapi/items.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    score = scrapy.Field()
    motto = scrapy.Field()
