import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello,世界,This is so good! This is FUCKing GREAT!")

def make_app():
    return tornado.web.Application(
        handlers=[
            (r"/", MainHandler)
        ],
        debug=True
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

