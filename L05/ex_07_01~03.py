import pymysql

db = pymysql.connect(host='localhost', user='root', password='password', db='sys', port=3306, charset='utf8')
cursor = db.cursor()#建立游标
cursor.execute("DROP TABLE IF EXISTS user")#如果有表叫user，删除表

sql = """
        create table user(            
        id int primary key,
        name char(20),
        sex char(10),
        age int,
        phone char(20)
        )
    """
try:
    # 执行SQL语句
    cursor.execute(sql)
    print("创建数据库成功")
except Exception as e:
    print("创建数据库失败：case%s" % e)
    exit()

#用sql语言写入数据表
sql1 = """
    insert into user values (1,'张三','男',20,'16666666666'),(2,'李四','女',18,'18888888888'),(3,'张明','男',27,'12345678901')
"""

# 执行 insert 增加的语句  如果出现异常对异常处理
try:
    cursor.execute(sql1)
    db.commit() #进行数据库提交，写入数据库
    print("插入数据成功")
except Exception as e:
    print("插入失败：case%s" % e)