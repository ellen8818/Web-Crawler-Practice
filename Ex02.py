# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:55:33 2021

@author: USER
"""

import db 

from bs4 import BeautifulSoup
import requests

url = 'https://tw.buy.yahoo.com/category/31372619'

header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }

data = requests.get(url,headers=header)
data.encoding = 'UTF-8'

data = data.text

soup = BeautifulSoup(data,'html.parser')

goods = soup.find_all('li',class_='BaseGridItem__grid___2wuJ7 BaseGridItem__multipleImage___37M7b')


for row in goods:
    title = row.find('span',class_='BaseGridItem__title___2HWui').text
    price = row.find('em').text
    price = price.replace('$','').replace(',','')
    img = row.img.get('srcset').split()[0]
    link = row.a.get('href')
    
    
    sql  = "select price from product where link='{}'".format(link)
    
    db.cursor.execute(sql)
    db.conn.commit()
    
    if db.cursor.rowcount == 0:
        sql = "insert into product(shop,name,price,photo_url,link,product_type) values('Yahoo','{}','{}','{}','{}',1)".format(title,price,img,link)
        
        db.cursor.execute(sql)
        db.conn.commit() #提交
    else:
        result = db.cursor.fetchone()
        
        if result[0] != int(price):
            print('修改')
    
   
    # print(title)
    # print(price)
    # print(img)
    # print(link)
    # print()
    
db.conn.close()    
    
    
    
    
    
