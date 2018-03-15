#!/usr/bin/env python
# coding=utf-8


#引入模块
import tornado.httpserver #此模块用来解决web服务的http协议问题，实现客户端和服务器端端互通
import tornado.ioloop #实现非阻塞socket循环，不能互通一次就结束
import tornado.options #命令行解析模版
import tornado.web #提供了一个简单的web框架与异步功能，从而使其扩展到大量打开到连接，使其成为理想的长轮询

from tornado.options import define,options #引入模块
define("port",default=8000,help = "run on the given port",type=int) #define定义了访问本服务器的端口，就是当在浏览器地址栏中输入localhost:8000的时候才能访问本网站，http协议默认端口说80，此处设置为8000以防端口冲突

#定义请求处理程序类 IndexHandler，专门应付客户的想服务器提出请求，服务器响应晨曦来接收并处理请求，以及反馈相关信息
#tornado.web.RequestHandler定义get()和set()方法。
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument("greeting","Hello Linda") #获取url中的参数
        self.write(greeting + ", welcome you to read:www.baidu.com") #输出get_argument获取的值 向客户的反馈信息

if __name__ == "__main__":
    tornado.options.parse_command_line()
    #(r"/",IndexHandler)－－ 根目录localhost:8000  ||| (r"/qiwsir/(.*)",QiwsirHandlers) －－其他目录
    app = tornado.web.Application(handlers=[(r"/",IndexHandler)]) #实例化application类，本质上说建立了整个网站程序的请求处理集合，然后可以背HTTPServer作为参数调用，实现http协议服务器访问。
    http_server = tornado.httpserver.HTTPServer(app) #执行HTTPServer一般要回调Application对象，并提供发送响应的借口，
    http_server.listen(options.port) 
    tornado.ioloop.IOLoop.instance().start() #一般此句放在__main__函数的最后一句，表示可以接收来自HTTP的请求了。
