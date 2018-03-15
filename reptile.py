#!/usr/bin/python
#-*- coding:utf8 -*-

import urllib2
from bs4 import BeautifulSoup
import MySQLdb as db
import random
#数据库类
class conndb(object):

    def __init__(self):
        self.conndb = db.Connect(host='127.0.0.1',port=3306,db='blog',charset='utf8',user='root',passwd='root')

    def add(self,parm):
        try:
            cursor = self.conndb.cursor()
            #print random.randint(1, 3)
            #return
            sql = "insert into  blog_model_article(title,date_time,content,digest,view,comment,author_id,picture,category_id,tj) values('%s','2018-03-09','%s',\"1\",\"1\",1,1,\"1\",'%s',1)" % (parm[0],parm[1],random.randint(1, 3))
            #print sql
            #return
            cursor.execute(sql)
            self.conndb.commit()
        except Exception as e:
            print e
#抓取页面
class paspage(conndb):

    #html
    def passpage(self,website):
        webdata = urllib2.urlopen(website)
        self.html = webdata.read()
        return self

    #获取主页面的链接
    def zepage(self):
        #print self.html;
        htmls = BeautifulSoup(self.html,'html.parser')
        del self.html
        postTitles = htmls.find_all('a',class_='postTitle2')
        for i in postTitles:
            data = self.detailpage(i.get('href')).detailpageadd()
            self.add(data)

    def detailpage(self,website):
        #return website
        webdata = urllib2.urlopen(website)
        #return webdata.read()
        self.detilehtml = webdata.read()
        return self

    def detailpageadd(self):
        # print self.html;
        htmls = BeautifulSoup(self.detilehtml, 'html.parser')
        del self.detilehtml
        postTitles = htmls.find('a', class_='postTitle2')
        postHtml = htmls.find('div', class_='blogpost-body')
        return [postTitles.get_text(),postHtml]


if __name__=="__main__":
    count = 1
    while(count<5):

        html = paspage().passpage('http://www.cnblogs.com/wanpython/default.html?page=%s'%(count)).zepage()
        count += 1






