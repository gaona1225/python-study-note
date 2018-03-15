#!/usr/bin/env python
# coding=utf-8

#the url structure of website -- 设置网站目录

import sys 
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler  
from handlers.user import UserHandler

url = [ #配置所有目录和对应的处理类
	(r'/',IndexHandler), #网站根目录
	(r'/user',UserHandler)
]
