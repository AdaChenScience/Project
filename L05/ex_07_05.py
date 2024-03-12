import pymysql

db = pymysql.connect(host='localhost', user='root', password='password', db='sys', port=3306, charset='utf8')
cursor = db.cursor()#建立游标

#查询所有数据
sql1 = """
    select name from user
"""
try:
    cursor.execute(sql1)
    ret=cursor.fetchall()
    for i in ret:
        print(i[0],end=' ')
    print()
except Exception as e:
    print("查询失败：case%s" % e)

#sql语句执行删除操作
sql = """
    delete from user where name like '%张%'
"""

try:
    cursor.execute(sql)
    db.commit()
    print('删除成功')
except Exception as e:
    print("删除失败：case%s" % e)

#查询所有数据
try:
    cursor.execute(sql1)
    ret=cursor.fetchall()
    for i in ret:
        print(i[0],end=' ')
except Exception as e:
    print("查询失败：case%s" % e)