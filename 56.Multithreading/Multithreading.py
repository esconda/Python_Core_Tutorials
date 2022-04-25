# Author: Burak Dogancay
import threading
import sys
import socketserver
from http.server import HTTPServer, SimpleHTTPRequestHandler,BaseHTTPRequestHandler

def runSimpleHttpServer():
  HandlerClass = SimpleHTTPRequestHandler
  ServerClass = HTTPServer
  Protocol = "HTTP/1.0"
  
  if sys.argv[1:]:
    port = int(sys.argv[1])
  else:
    port = 8000
  server_address = ('127.0.0.1', port)
  HandlerClass.protocol_version = Protocol
  httpd = ServerClass(server_address, HandlerClass)
  
  sa = httpd.socket.getsockname()
  print ("Serving HTTP on", sa[0], "port", sa[1], "...")
  httpd.serve_forever()
  
def servingFiles():
    #The SocketServer module provides the classes and functionalities to setup a network server.
    #SocketServer's TCPServer class sets up a server using the TCP protocol. The constructor accepts a tuple
    #representing the address of the server (i.e. the IP address and port) and the class that handles the server requests.
    #The SimpleHTTPRequestHandler class of the SimpleHTTPServer module allows the files at the current directory to be served
    PORT = 8000
    handler = SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler) #This uses the internet TCP protocol, which provides for continuous streams of data between the client and server.
    print("--SOCKET SERVER--")
    print("serving at port", PORT)
    print("-----------------")
    httpd.serve_forever() #Handle requests until an explicit shutdown() request.
    
def getPostPutExample():
  class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
    def do_GET(self):
      self._set_headers()
      self.wfile.write("received get request")
    def do_POST(self):
      '''Reads post request body'''
      self._set_headers()
      content_len = int(self.headers.getheader('content-length', 0))
      post_body = self.rfile.read(content_len)
      self.wfile.write("received post request:<br>{}".format(post_body))
    def do_PUT(self):
      self.do_POST()
  host = ''
  port = 80
  HTTPServer((host, port), HandleRequests).serve_forever()

def main():
 #Networking
 #runSimpleHttpServer()
 #servingFiles()
 getPostPutExample()
 #---------------------------


if __name__ == '__main__':
    main()