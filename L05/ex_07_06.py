import pymysql

db = pymysql.connect(host='localhost', user='root', password='password', db='sys', port=3306, charset='utf8')
cursor = db.cursor()#建立游标

#sql语句
sql = """
    select avg(age) from user
"""

try:
    cursor.execute(sql)
    ret=cursor.fetchone()
    print(ret[0])
except Exception as e:
    print("查询失败：case%s" % e)