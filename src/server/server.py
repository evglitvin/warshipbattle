import json
from http.server import HTTPServer, BaseHTTPRequestHandler

from api.v1.utils import dispatch_handler


HOST = 'localhost'
PORT = 8000


class RequestHandler(BaseHTTPRequestHandler):
    print(f'Server is running on {HOST}:{PORT}...\n')

    def serv_reply(self, code, data):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        """
        :return: response for GET request depending on requested endpoint
        """
        dispatch_handler(self)

    def do_POST(self):
        """
        :return: response for POST request depending on requested endpoint
        """
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)
        dispatch_handler(self, data)


http_daemon = HTTPServer((HOST, PORT), RequestHandler)
http_daemon.serve_forever()
