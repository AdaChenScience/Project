import requests
import pandas as pd
import re
import pymysql
from lxml import etree

db = pymysql.connect(host='localhost', user='root', password='password', db='sys', port=3306, charset='utf8')
cursor = db.cursor()#建立游标
cursor.execute("DROP TABLE IF EXISTS douban")#如果有表叫douban，删除表

sql = """
        create table douban(            
        name char(50) not null,
        actor char(100),
        label char(100),
        year char(50),
        star char(10),
        evaluate char(20) ,
        introduction char(100)
        )
    """
try:
    # 执行SQL语句
    cursor.execute(sql)
    print("创建数据库成功")
except Exception as e:
    print("创建数据库失败：case%s" % e)
    exit()

# 爬虫
urls=['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]
headers={'User-Agent':'Mozilla/5.0 (x11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Safari/537.36'}

for url in urls:
    print('正在写入%d/%d'%(urls.index(url)+1,len(urls)))
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    infos=selector.xpath("//ol[@class='grid_view']/li")
    for info in infos:
        name=info.xpath(".//div[@class='item']//div[@class='info']//div[@class='hd']//a/span[1]/text()")[0].strip()
        actor=info.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//p[1]/text()[1]")[0].strip()
        information=info.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//p[1]/text()[2]")[0].strip()
        date=information.split('/')[0].strip()
        star=info.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//div/span[2]/text()")[0].strip()
        evaluate=info.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//div/span[4]/text()")[0].strip()
        try:
            introduction=info.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//p[2]/span/text()")[0].strip()
        except:
            introduction=''

        #用sql语言写入数据表
        sql1 = """
            insert into douban(
            name,
            actor,
            label,
            year,
            star,
            evaluate,
            introduction
            )value("%s","%s","%s","%s","%s","%s","%s")
        """ % (name,actor,information,date,star,evaluate,introduction)#将值插入到占位符%s

        # 执行 insert 增加的语句  如果出现异常对异常处理
        try:
            cursor.execute(sql1)
            db.commit() #进行数据库提交，写入数据库
        except Exception as e:
            print("写入失败：case%s" % e)

# 关闭游标连接
cursor.close()
# 关闭数据库连接
db.close()
print('写入成功！')