#!/usr/bin/env python
# coding=utf-8

import tornado.web
import tornado.gen
from base import BaseHandler

import time

class SleepHandler(tornabdo.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout,time.time() + 17)
		#yield tornado.gen.sleep(17)
		self.render("sleep.html")