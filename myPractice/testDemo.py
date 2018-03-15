#!/usr/bin/env python
#coding:utf-8
import smtplibfrom email.mime.text import MIMETextfrom email.header import Headersender = 'huochen1994@163.com'receiver = 'huochen1994@126.com'subject = 'python email test'smtpserver = 'smtp.163.com'username = 'huochen1994@126.com'password = '*********'msg = MIMEText( 'Hello Python', 'text', 'utf-8' )msg['Subject'] = Header( subject, 'utf-8' )smtp = smtplib.SMTP()smtp.connect( smtpserver )smtp.login( username, password )smtp.sendmail( sender, receiver, msg.as_string() )smtp.quit()
