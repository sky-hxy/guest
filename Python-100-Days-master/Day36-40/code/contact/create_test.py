'''
Author: hxy 1305149167@qq.com
Date: 2024-06-24 00:29:53
LastEditors: hxy 1305149167@qq.com
LastEditTime: 2024-06-25 00:42:02
FilePath: /Python-100-Days-master/Day36-40/code/contact/main_test.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import pymysql
no = int(input("部门编号："))
name = input("部门名称：")
location = input("部门所在地：")

# 创建数据库连接
conn = pymysql.connect(host='localhost', port=3306,
                       user='root', password='1998',
                       database='hrs', charset='utf8mb4')

try:
    # 获取游标
    with conn.cursor() as cursor:
        # 通过游标对象发起sql语句
        affected_rows = cursor.execute(
            'insert into `tb_dept` values (%s, %s, %s)',
            (no, name, location)
            )
        if affected_rows == 1:
            print("新增部门成功")
    # 提交事物
    conn.commit()
except pymysql.MySQLError as err:
    # 回滚
    conn.rollback()
    print(type(err), err)
finally:
    # 关闭释放资源
    conn.close()