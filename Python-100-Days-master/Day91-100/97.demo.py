'''
Author: hxy 1305149167@qq.com
Date: 2023-05-09 20:26:45
LastEditors: hxy 1305149167@qq.com
LastEditTime: 2023-05-09 20:40:53
FilePath: /Python-100-Days-master/Day91-100/97.demo.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import pymysql
from django.apps import AppConfig
from django.core.cache import cache

SELECT_PROVINCE_SQL = 'select distid, name from tb_district where pid is null'

class CommonConfig(AppConfig):
    name = 'common'

    # 缓存预热
    def ready(self):
        conn = pymysql.connect(host='1.2.3.4', port=3306,
                               user='root', password='pass',
                               database='db', charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor
                               )
        try:
            with conn.cursor() as cursor:
                cursor.execute(SELECT_PROVINCE_SQL)
                provinces = cursor.fetchall()
                cache.set('provinces', provinces)
        except Exception as e:
            raise e
        finally:
            conn.close()