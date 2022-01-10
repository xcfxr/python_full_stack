import pymysql


conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'day48',
    charset = 'utf8',
    autocommit = True
)
cursor = conn.cursor(pymysql.cursors.DictCursor)
# 调用存储过程
cursor.callproc('p1',(1,5,10))
"""
@_p1_0=1
@_p1_1=5
@_p1_2=10
"""
# print(cursor.fetchall())
cursor.execute('select @_p1_2;')
print(cursor.fetchall())