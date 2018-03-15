#!/usr/bin/env python
# coding=utf-8

#网站系统的基本配置，建立网站的请求你处理集合
from url import url
import tornado.web
import os


settings = dict(
	template_path = os.path.join(os.path.dirname(__file__),"templates"),
	static_path = os.path.join(os.path.dirname(__file__),"statics"),
	cookie_secret = "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=" , #为设置的cookie加密
	xsrf_cookies = True, #使用xsrf_cookie参数开启XSRF保护
	login_url = "/"
	)

application = tornado.web.Application(
	handlers = url,
	**settings  
	)