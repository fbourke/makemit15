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
		self.write(unicode("""
<!DOCTYPE html>
<html>
  <head>
    <title>SLAMBot with Team40</title>
  	<meta charset="UTF-8">
  </head>
  <body>
	<style type="text/css">
	.tg  {border-collapse:collapse;border-spacing:0;}
	.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
	.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
	</style>
	<table class="tg">
	  <tr>
	    <th class="tg-031e"></th>
	    <th class="tg-031e">↑</th>
	    <th class="tg-031e"></th>
	  </tr>
	  <tr>
	    <td class="tg-031e">←</td>
	    <td class="tg-031e"><img src='/image'></td>
	    <td class="tg-031e">→</td>
	  </tr>
	  <tr>
	    <td class="tg-031e"></td>
	    <td class="tg-031e"></td>
	    <td class="tg-031e"></td>
	  </tr>
	</table>
  </body>
</html>

"""))

application = tornado.web.Application([
	(r"/image", ImageHandler),
	(r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
