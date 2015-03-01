#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
from PIL import Image
import tornado.ioloop
import tornado.web
import serial
import mraa

class ImageHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Content-type', 'image/png')
        #self.set_header('Content-length', len(s))   
	filename = "img.png"
	with open(filename) as f:
		self.write(f.read())	

class UpHandler(tornado.web.RequestHandler):
	def get(self):
		self.write(unicode("""
			<!DOCTYPE html>
			<html>
			  <head>
			    <meta http-equiv="refresh" content="0; url=/" />	
			  </head>
			</html>"""))
	asdf = serial.Serial('/dev/ttyMFD1',115200)
	asdf.write("0f1000f1f100")
	asdf.write("1f1000f1f100")


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write(unicode("""
<!DOCTYPE html>
<html>
  <head>
    <title>SLAMBot with Team40</title>
  	<meta charset="UTF-8">
  	<META HTTP-EQUIV="refresh" CONTENT="5">
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
	    <th class="tg-031e"><a href='/up'>↑</a></th>
	    <th class="tg-031e"></th>
	  </tr>
	  <tr>
	    <td class="tg-031e">←</td>
	    <td class="tg-031e"><img src='/image'></td>
	    <td class="tg-031e">→</td>
	  </tr>
	  <tr>
	    <td class="tg-031e"></td>
	    <td class="tg-031e">⇓</td>
	    <td class="tg-031e"></td>
	  </tr>
	</table>
  </body>
</html>

"""))

application = tornado.web.Application([
	(r"/image", ImageHandler),
	(r"/up", UpHandler),
	(r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
