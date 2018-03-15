#!/usr/bin/env python
#coding:utf-8   #强制使用utf-8编码格式
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender='gnp1225@163.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user='476343445@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
def mail():
    ret=True
    print "111"
    print ret
    try:
        print "try-1"
        msg=MIMEText('python send email test haha -- 476343445 －－ success','plain','utf-8')
        print "try-2"
        msg['From']=formataddr(["gnp1225",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        print "try-3"
        msg['To']=formataddr(["476343445",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号－－此处昵称需要写476343445，这个可以选择用网易邮箱向qq邮箱发送邮件试试，发现昵称不是沐是476343445
        print "try-4"
        msg['Subject']="python email--success" #邮件的主题，也可以说是标题

        print "try-5"
        server=smtplib.SMTP("smtp.163.com",25)  #发件人邮箱中的SMTP服务器，端口是25
        print "try-6"
        server.login(my_sender,"gnp1225")    #括号中对应的是发件人邮箱账号、邮箱密码－－此处密码为设置的smtp授权码非网易邮箱登录密码
        print "try-7"
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        print "try"
        server.quit()   #这句是关闭连接的意思
    except Exception,e:   #如果try中的语句没有执行，则会执行下面的ret=False
        print "exception"
        print e
        ret=False
    return ret

ret=mail()
print "call fn"
print ret
if ret:
    print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
else:
    print("filed")  #如果发送失败则会返回filed
