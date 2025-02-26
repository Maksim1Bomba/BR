from http.server import BaseHTTPRequestHandler
from io import BytesIO

class HTTPResponseParse(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = BytesIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def parse_request(self):
        return self.headers.keys() # проблема здесь, он не видит headers
    
    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message

text = """POST / HTTP/1.1
host: 127.0.0.1:8082
connection: keep-alive
content-type: text/plain;charset=UTF-8
accept: */*
accept-language: *
sec-fetch-mode: cors
user-agent: undici
accept-encoding: gzip, deflate
content-length: 22

{"data": "blalallala"}
"""
text = text.encode()

request = HTTPResponseParse(text)

# print(request.headers.keys()) # отдельно все работает
# print(request.parse_request()) # а вот так не хочет
