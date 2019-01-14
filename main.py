#! /usr/bin/env python3
# encoding: utf-8
# author:Shelly
# time:2019-01-14
from sys import path
from  http.server import HTTPServer,BaseHTTPRequestHandler
import demjson

'''
只接收post数据：
{'action':'print','charset':'utf-8','postData':{'url':url,'host':host,'port':port,'protocol':protocol,'headers':headers_dict,'body':body_str}}
'''

class ServerHTTP(BaseHTTPRequestHandler):

	#默认回显
	def creat_wfile(self):
		self.send_response(200)
		self.send_header('Content-type','text/html; charset=utf-8')
		self.send_header('Content-Length',str(len(self.data)))
		self.end_headers()
		self.wfile.write(bytes(self.data, encoding='utf-8'))

    #处理get请求：不支持
	def do_GET(self):
		self.data = '{"status":1,"error":"Only supprt POST"}'
		self.creat_wfile()

	#接收数据
	def do_POST(self):
		self.webName = str(self.path.split('/')[1])
		if self.postDataApi():
			length = int(self.headers['content-length'])
			postData = self.rfile.read(length) 
			print (postData)
			print (demjson.decode(postData))
			self.data = '{"status":0,"error":""}'
			self.creat_wfile()
		else:
			self.data = '{"status":1,"error":"API not exist!"}'
			self.creat_wfile()

	#api
	def postDataApi(self):
		if self.webName == 'postDataApi':
			return True
		else:
			return False


def start_server(port):
	http_server = HTTPServer(('', int(port)),ServerHTTP)
	http_server.serve_forever() 

#在1858端口开启http服务
if __name__ == "__main__":
	start_server(1858)

str123 = "{'url':"+url+",'host':"+host+",'port':"+port+",'protocol':"+protocol+",'headers':"+headers+",'body':"+body_str+"}"
