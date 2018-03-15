#!/usr/bin/env python
# coding=utf-8

import sqlite3 #引入sqlite3关联数据库
conn = sqlite3.connect("sqliteDB.db") #如果已经有了sqliteDB.db就建立连接，如果没有就创建此数据库，可以再当前目录D:/study/python/myTest目录下生成了sqliteDB.db
cur = conn.cursor() #建立游标对象

create_table = "create table books(title text,author text,lang text)" #创建数据库表
cur.execute(create_table)

cur.execute("insert into books values('from beginner to master','laoqi','python')") #建立表books

cur.execute("select * from books") #查询books表数据
print cur.fetchall() #output [(u'from beginner to master', u'laoqi', u'python'), (u'from beginner to master', u'laoqi', u'python')]

#批量插入
books = [("first book","first","c"),("second book","second","c"),("third book","second","python")]
cur.executemany("insert into books values(?,?,?)",books)

cur.execute("update books set title='physics' where author = 'first'") #更新表字段

cur.execute("delete from books where author = 'second'") #删除表字段
rows = cur.execute("select * from books")
#print cur.fetchall() #output [(u'from beginner to master', u'laoqi', u'python'), (u'from beginner to master', u'laoqi', u'python'), (u'first book', u'first', u'c'), (u'second book', u'second', u'c'), (u'third book', u'second', u'python'), (u'from beginner to master', u'laoqi', u'python')]
for row in rows:
    print row

    

#保存数据
conn.commit() #提交保存
cur.close() #关闭游标对象
conn.close() #关闭连接

