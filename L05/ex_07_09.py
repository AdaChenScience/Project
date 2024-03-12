import pymysql

db = pymysql.connect(host='localhost', user='root', password='password', db='sys', port=3306, charset='utf8')
cursor = db.cursor()#建立游标

#sql语句
sql = """
    select name from user,team,score where user.id=score.userid and team.id=score.teamid and team.teamName like 'ECNU' and user.age<20
"""

try:
    cursor.execute(sql)
    ret=cursor.fetchall()
    for i in ret:
        print(i[0])
except Exception as e:
    print("查询失败：case%s" % e)