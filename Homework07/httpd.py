import asyncore
import asynchat
import socket
import multiprocessing
import logging
import mimetypes
import os
from urlparse import parse_qs
import urllib
import argparse
from time import strftime, gmtime
def url_normalize(path):
if path.startswith("."):
path = "/" + path
while "../" in path:
p1 = path.find("/..")
p2 = path.rfind("/", 0, p1)
if p2 != -1:
path = path[:p2] + path[p1+3:]
else:
path = path.replace("/..", "", 1)
path = path.replace("/./", "/")
path = path.replace("/.", "")
return path


class FileProducer(object):


def __init__(self, file, chunk_size=4096):
    self.file = file
    self.chunk_size = chunk_size

def more(self):
    if self.file:
        data = self.file.read(self.chunk_size)
        if data:
            return data
        self.file.close()
        self.file = None
    return ""

class AsyncServer(asyncore.dispatcher):


def __init__(self, host="127.0.0.1", port=9000):
    pass

def handle_accepted(self):
    pass

def serve_forever(self):
    pass

class AsyncHTTPRequestHandler(asynchat.async_chat):


def __init__(self, sock):
    super().__init__(sock)
        self.ibuffer = ''
        self.obuffer = b''
        self.set_terminator(b'\r\n\r\n')
        self.reading_headers = True
        self.request = ''
        self.headers = {}
        self.method = ''
        self.path = ''
        self.response = ''
        self.server_name = 'localhost'
        self.server_port = 9000

def collect_incoming_data(self, data):
    logging.debug(f"Incoming data: {data}")
        if not self.reading_headers:
            self.obuffer = data
        else:
            self.ibuffer += data.decode('utf-8')

def found_terminator(self):
    self.parse_request()

def parse_request(self):
        if self.headers == {}:
            headers_key = self.parse_headers()
            if not headers_key:
                self.send_error(400, 'Bad Request')
            if self.method == 'POST':
                if not ('Content-Length' in self.headers) or not (int(self.headers['Content-Length']) > 0):
                    self.handle_request()
            else:
                self.handle_request()
        else:
            self.handle_request(

def parse_headers(self):
    headers = header.split('\r\n')

        try:
            self.headers = dict([(i.split(':')[0], i.split(':')[1][1:]) for i in headers[1:]])
            self.method = headers[0].split()[0]
            self.query = headers[0].split()[1]
            self.protocol = headers[0].split()[2]
        except:
            return False
        return True

def handle_request(self):
    method_name = 'do_' + self.method
        if not hasattr(self, method_name):
            self.send_error(405)
            self.handle_close()
            return
        handler = getattr(self, method_name)
        handler()

def send_header(self, keyword, value):
    pass

def send_error(self, code, message=None):
    try:
            short_msg, long_msg = self.responses[code]
        except KeyError:
            short_msg, long_msg = '???', '???'
        if message is None:
            message = short_msg
    
    self.init_response(code, message)
        self.add_header("Content-Type", "text/plain")
        self.add_header("Connection", "close")
        self.end_headers()
        self.send(bytes(self.response.encode('utf-8')))
        self.close()

def send_response(self, code, message=None):
    self.response_body = (code, message)
        return

def end_headers(self):
    self.response += "\r\n"

def date_time_string(self):
    return strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())

def send_head(self):
            path = self.translate_path('public/' + self.request)

        if os.path.isdir(path):
            path = os.path.join(path, "index.html")
            if not os.path.exists(path):
                self.init_response(403)
                self.handle_close()
                return None

        try:
            file = bytes()
            fp = FileProducer(open(path, 'rb'))
            while True:
                cur_chunk = fp.more()
                if not cur_chunk:
                    break
                file += cur_chunk
        except IOError:
            self.init_response(404)
            self.send(bytes(self.response.encode('utf-8')))
            self.handle_close()
            return None

        _, ext = os.path.splitext(path)
        ctype = mimetypes.types_map[ext.lower()]

        self.init_response(200)
        self.add_header("Content-Type", ctype)
        self.add_header("Content-Length", os.path.getsize(path))
        self.end_headers()
        return file

def translate_path(self, path):
    return url_normalize(path)

def do_GET(self):
    f = self.send_head()
        if f:
            self.send(bytes(self.response.encode('utf-8')) + f)
            self.close()

def do_HEAD(self):
    f = self.send_head()
        if f:
            self.send(bytes(self.response.encode('utf-8')))
            self.close(

responses = {
    200: ('OK', 'Request fulfilled, document follows'),
    400: ('Bad Request',
        'Bad request syntax or unsupported method'),
    403: ('Forbidden',
        'Request forbidden -- authorization will not help'),
    404: ('Not Found', 'Nothing matches the given URI'),
    405: ('Method Not Allowed',
        'Specified method is invalid for this resource.'),
}

def parse_args():
parser = argparse.ArgumentParser("Simple asynchronous web-server")
parser.add_argument("--host", dest="host", default="127.0.0.1")
parser.add_argument("--port", dest="port", type=int, default=9000)
parser.add_argument("--log", dest="loglevel", default="info")
parser.add_argument("--logfile", dest="logfile", default=None)
parser.add_argument("-w", dest="nworkers", type=int, default=1)
parser.add_argument("-r", dest="document_root", default=".")
return parser.parse_args()


def run():
server = AsyncServer(host=args.host, port=args.port)
server.serve_forever()


if name == "main":
args = parse_args()


logging.basicConfig(
    filename=args.logfile,
    level=getattr(logging, args.loglevel.upper()),
    format="%(name)s: %(process)d %(message)s")
log = logging.getLogger(__name__)

DOCUMENT_ROOT = args.document_root
for _ in xrange(args.nworkers):
    p = multiprocessing.Process(target=run)
    p.start()