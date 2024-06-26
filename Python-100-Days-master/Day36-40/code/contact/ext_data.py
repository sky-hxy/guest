'''
Author: hxy 1305149167@qq.com
Date: 2024-06-25 23:38:27
LastEditors: hxy 1305149167@qq.com
LastEditTime: 2024-06-26 00:43:42
FilePath: /Python-100-Days-master/Day36-40/code/contact/ext_data.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import pymysql
import openpyxl
import os

# 创建工作簿对象
workbook = openpyxl.Workbook()
# 获得默认的工作表
sheet = workbook.active
# 修改工作表的标题
sheet.title = '员工基本信息'
# 给工作表添加表头
sheet.append(('工号', '姓名', '职位', '月薪', '补贴', '部门'))
# 创建连接
conn = pymysql.connect(host='localhost', port=3306,
                       database='hrs',user='root',
                       password='1998',charset='utf8mb4')
# 获取游标对象
try:
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT `eno`, `ename`, `job`, `sal`, COALESCE(`comm`, 0), `dno` FROM `tb_emp` natural join `tb_dept`'
            )
        row = cursor.fetchone()
        while row:
            # 讲数据逐行添加到工作表中
            sheet.append(row)
            row = cursor.fetchone()

    workbook.save('hrs.xlsx')
    path = '/Users/subai/Documents/Code/pyTest/Python-100-Days-master/Day36-40/code/contact'
    file_path = os.path.join(path, 'hrs.xlsx')
    print('文件已保存到当前工作目录：', path)

except pymysql.MySQLError as e:
    print(type(e), e)

finally:
    conn.close()