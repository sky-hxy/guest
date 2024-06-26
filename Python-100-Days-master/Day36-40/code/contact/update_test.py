import pymysql
no = int(input('请输入部门编号：'))
name = input('请输入部门名称：')
address = input('请输入部门地址：')

conn = pymysql.connect(host='localhost', port=3306, user='root', password='1998',database='hrs',charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        affected_rows = cursor.execute(
            'update `tb_dept` SET `dname` = %s, `dloc` = %s where `dno` = %s',(name, address, no,)
            )
        
        if affected_rows == 1:
            print('更新数据成功')
            conn.commit()
except pymysql.MySQLError as err:
    print(type(err), err)
finally:
    conn.close()