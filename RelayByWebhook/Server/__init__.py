from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler


class Server(HTTPServer):
    def __init__(self,portId,src,dst):
        HTTPServer.__init__(self,("",int(portId)),RequestHandler)
        self.src = src
        self.dst = dst
        try:
            self.serve_forever()
        except KeyboardInterrupt:
            self.socket.close()


class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self,request,client_address,server):
        BaseHTTPRequestHandler.__init__(self,request,client_address,server)
        self.server = server
    def do_GET(self):
        try:
            self.SendAck()
        except Exception,error:
            self.SendErr(error)
    def do_POST(self):
        try:
            data = self.rfile.read(int(self.headers.getheader("content-length")))
            message = self.server.src.rx(data)
            log("RX",message)
            log("TX",self.server.dst.tx(message["from"],message["text"]))
            self.SendAck()
        except Exception,error:
            self.SendErr(error)
    def SendAck(self):
        self.send_response(200)
        self.send_header("content-type","text/plain")
        self.send_header("cache-control","no-cache")
        self.end_headers()
        self.wfile.write("{}")
    def SendErr(self,error):
        self.send_error(500,error.message)


def log(prefix,message):
    if message:
        print prefix+" ["+ascii(message["from"])+": "+ascii(message["text"])+"]"


def ascii(string):
    return string if isinstance(string,str) else string.encode("utf-8")
