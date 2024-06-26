'''
Author: hxy 1305149167@qq.com
Date: 2024-06-25 22:35:45
LastEditors: hxy 1305149167@qq.com
LastEditTime: 2024-06-25 22:57:17
FilePath: /Python-100-Days-master/Day36-40/code/contact/delete_test.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import pymysql

no = int(input("请输入要删除的部门编号："))

# 创建连接
conn = pymysql.connect(host= 'localhost', port=3306, user='root', password='1998',database='hrs' , charset='utf8mb4')

# 操作数据库
try:
    with conn.cursor() as cursor:
        affected_rows = cursor.execute(
            'delete from `tb_dept` where `dno` = %s',(no,)
            )
        if affected_rows == 1:
            print(f'删除部门：{no}成功')

        conn.commit()
        
except pymysql.MySQLError as err:
    conn.rollback()
    print(type(err), err)

finally:
    conn.close()