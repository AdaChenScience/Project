import pymysql

db = pymysql.connect(host='localhost', user='root', password='password', db='sys', port=3306, charset='utf8')
cursor = db.cursor()#建立游标

#sql语句
sql = """
    select name from user where age>=20 and age<=30 and name like '%张%' order by age desc
"""

try:
    cursor.execute(sql)
    ret=cursor.fetchall()
    for i in ret:
        print(i[0])
except Exception as e:
    print("查询失败：case%s" % e)