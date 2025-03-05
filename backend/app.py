import socket
import sys
import threading

from parser import HTTPRequest
from response import MakeHTTPResponse
from hello import hello

class Server:
    def __init__(self, server_addr):
        self.server_addr = server_addr
        self.paths = {}
    
    def start(self):
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock.bind(self.server_addr)
        self.lsock.listen()
        print(f"Listening on {self.server_addr}")

        while True:
            conn, addr = self.lsock.accept()
            thread = threading.Thread(target=self.service_connection, args=(conn, addr))
            thread.start()

    def service_connection(self, conn, addr):
        print(f"Open connection on {addr}")
        connected = True
        data = ''
        
        out = conn.recv(1024)
        if not out:
            connected = False
        else:
            data += out.decode()

        print(data)
            
        if connected:
            request = HTTPRequest(data)
            if request.path in self.paths.keys():
                json = self.paths[request.path]()
                makeResponse = MakeHTTPResponse(200, json)
            else:
                makeResponse = MakeHTTPResponse(404, '')
                
            response = makeResponse.make()
            print(response.decode())
            while response:
                sent = conn.send(response)
                response = response[sent:]
        print(f"Close connection on {addr}")
        conn.close()

    def add_path(self, path, func):
        self.paths[path] = func

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = 8080
    server = Server((ip, port))
    try:
        server.add_path('/hello', hello)
        server.start()
    except KeyboardInterrupt:
        sys.exit(0)
        
    

