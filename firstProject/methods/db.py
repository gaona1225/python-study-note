#!/usr/bin/env python
# coding=utf-8

#连接数据库


import sqlite3
conn = sqlite3.connect("sqliteDB.db") 
cur = conn.cursor()


"""import MySQLdb

conn = MySQLdb.connect(host="localhost",user="root",passwd="123123",db="qiwsirtest",port=3306,charset="utf-8")
cur = conn.cursor()"""
