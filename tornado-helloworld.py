import io
from PIL import Image
import tornado.ioloop
import tornado.web

class ImageHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Content-type', 'image/jpg')
        #self.set_header('Content-length', len(s))   
	filename = "img.jpg"
	with open(filename) as f:
		self.write(f.read())	

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("<html><body><img src='/image'></body></html>")

application = tornado.web.Application([
	(r"/image", ImageHandler),
	(r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
