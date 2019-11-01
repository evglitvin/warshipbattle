import json
from http.server import HTTPServer, BaseHTTPRequestHandler

from src.api.endpoints_const import SIGN_UP, LOGIN


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def _get_payload(self):
        content_length = int(self.headers.get('Content-Length'))
        return self.rfile.read(content_length)

    def get_user_data(self):
        pass

    def do_POST(self):
        response = {}
        if self.path == SIGN_UP:
            if not self.is_user_exists():
                self.create_user()
            else:
                response = {'status_code': 409, 'msg': 'such login is not allowed'}
        elif self.path == LOGIN:
            token = self.get_auth_token()
            if token:
                response = {'status_code': 200, 'oauth': token}
            else:
                response = {'status_code': 400, 'msg': 'login or password is wrong'}

        self.wfile.write(bytes(json.dumps(response), 'utf-8'))



def run(serever_cls=HTTPServer, handler_cls=BaseHTTPRequestHandler):
    server_addr = ('', 8051)
    http = serever_cls(server_addr, handler_cls)
    http.serve_forever()
