import requests
import pandas as pd
import re
from lxml import etree
import csv

fp=open('./douban.csv','w',encoding='utf-8')
writer=csv.writer(fp)
writer.writerow(['影片名','演员','标签','年份','评分','评分人数','热门影评'])

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
        writer.writerow([name,actor,information,date,star,evaluate,introduction])

fp.close()
