import tornado.web
import tornado.ioloop
import os.path

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("sea.html")
settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    debug = True
)

application = tornado.web.Application([
    (r"/sea", MainHandler)
],**settings)

if __name__ == "__main__":
    application.listen(8887)
    print("I'm listening on port 8887")
    tornado.ioloop.IOLoop.instance().start()