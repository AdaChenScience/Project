import pymysql

db = pymysql.connect(host='localhost', user='root', password='password', db='sys', port=3306, charset='utf8')
cursor = db.cursor()#建立游标
cursor.execute("DROP TABLE IF EXISTS team")#如果有表叫team，删除表
cursor.execute("DROP TABLE IF EXISTS score")#如果有表叫score，删除表

sql1 = """
        create table team(            
        id int primary key,
        teamName char(20)
        )
    """
sql2 = """
        create table score(            
        id int primary key,
        teamid int,
        userid int,
        score int,
        constraint con1 foreign key(teamid) references team(id),
        constraint con2 foreign key(userid) references user(id)
        )
    """

try:
    # 执行SQL语句
    cursor.execute(sql1)
    cursor.execute(sql2)
    print("创建数据库成功")
except Exception as e:
    print("创建数据库失败：case%s" % e)
    exit()

#用sql语言写入数据表
sql3 = """
    insert into team values (1,'ECNU'),(6,'SJTU')
"""
sql4 = """
    insert into score values (1,1,2,5),(2,1,3,12),(3,6,1,8)
"""

# 执行 insert 增加的语句  如果出现异常对异常处理
try:
    cursor.execute(sql3)
    cursor.execute(sql4)
    db.commit() #进行数据库提交，写入数据库
    print("插入数据成功")
except Exception as e:
    print("插入失败：case%s" % e)