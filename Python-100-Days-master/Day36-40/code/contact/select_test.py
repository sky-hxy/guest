import pymysql
def select_database(name):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='1998', database='hrs',charset='utf8mb4')



    try:
        with conn.cursor() as cursor:
            cursor.execute(
                'select * from `tb_dept` where `dname` = %s',(name,)
                )
        # 通过游标对象获取数据
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()
    except pymysql.MySQLError as err:
        print(type(err), err)

    finally:
        conn.close()

name = input('请输入部门名称：')
select_database(name)