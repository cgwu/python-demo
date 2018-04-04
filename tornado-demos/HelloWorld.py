#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.httpclient
#from tornado.httpclient import AsyncHTTPClient

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello,世界,This is so good! This is GREAT!")

class StoryHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db=db

    def get(self, story_ids):
        self.write('this is story %s from db %s' % (story_ids, self.db))

class FetchAsyncHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        #http = AsyncHTTPClient()
        #response = yield http.fetch('http://www.baidu.com/')
        response = yield http.fetch('http://www.163.com/')
        self.write(response.body)

def make_app():
    return tornado.web.Application(
        handlers=[
            (r"/", MainHandler),
            (r"/baidu", FetchAsyncHandler),
            (r"/story/([0-9]+)", StoryHandler, dict(db='foodb')),
        ],
        debug=True
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

