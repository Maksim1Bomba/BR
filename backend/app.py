import socket
import sys
import select

from parser import HTTPRequest
from response import MakeHTTPResponse
from hello import hello

class Server:
    def __init__(self, server_addr):
        self.server_addr = server_addr
        self.paths = {}
        self.sockets_list = []
    
    def start(self):
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock.bind(self.server_addr)
        self.lsock.listen(5)
        self.sockets_list.append(self.lsock)
        print(f"Listening on {self.server_addr}")

        while True:
            read_sockets, _, _ = select.select(self.sockets_list, [], [])
            for notified_socket in read_sockets:
                if notified_socket == self.lsock:
                    conn, addr = self.lsock.accept()
                    print(f"Accepted new connection from module import symbol {addr}")
                    self.sockets_list.append(conn)
                else:
                    self.service_connection(notified_socket)
                
    def service_connection(self, conn):
        message = conn.recv(1024)
        request = message
        while not b'\r\n\r\n' in message:
            print(message)
            request += message
            message = conn.recv(1024)
        print(request.decode())

        if request:
            request = HTTPRequest(request.decode())
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
                
        print(f"Close connection")
        self.sockets_list.remove(conn)
        conn.close()

    def add_path(self, path, func):
        self.paths[path] = func

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = 8082
    server = Server((ip, port))
    try:
        server.add_path('/hello', hello)
        server.start()
    except KeyboardInterrupt:
        sys.exit(0)
        
    


