import async_server
import os
import sys


class AsyncWSGIServer(httpd.AsyncServer):

    def set_app(self, application):
        self.application = application

    def get_app(self):
        return self.application


class AsyncWSGIRequestHandler(httpd.AsyncHTTPRequestHandler):

    def get_environ(self):
                environ = {
         'wsgi.version': (1, 0),
         'wsgi.url_scheme': 'http',
         'wsgi.input': sys.stdin,
         'wsgi.errors': sys.stderr,
         'wsgi.multithread': False,
         'wsgi.multiprocess': False,
         'wsgi.run_once': False,
         'REQUEST_METHOD': self.method,
         'PATH_INFO': self.path,
         'SERVER_NAME': self.server_name,
         'SERVER_PORT': str(self.server_port)
              }

        return environ

    def start_response(self, status, response_headers, exc_info=None):
        code, message = status.split(" ")[:2]
        self.init_response(code, message)

        for key, value in headers:
            self.add_header(key, value)

        self.end_headers()

    def handle_request(self):
        env = self.get_environ()
        app = server.get_app()
        result = app(env, self.start_response)
        self.finish_response(result)

    def finish_response(self, result):
        self.send(bytes(self.response.encode('utf-8')) + result[0])
        self.close()