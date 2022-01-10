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

# 增
sql = 'insert into user(name,password) values(%s,%s)'
# rows = cursor.execute(sql,('jackson',123))
rows = cursor.executemany(sql,[('xxx',123),('ooo',123),('yyy',123)])
print(rows)
# conn.commit()  # 确认
# 修改
# sql = 'update user set name="jasonNB" where id=1'
# rows = cursor.execute(sql)
# print(rows)
# conn.commit()  # 确认
# 删除
sql = 'delete from user where id=7'
rows = cursor.execute(sql)
print(rows)
conn.commit()  # 确认
# 查
# sql = 'select * from user'
# cursor.execute(sql)
# print(cursor.fetchall())

"""
增删改查中
    删改增它们的操作设计到数据的修改 
    需要二次确认
"""


