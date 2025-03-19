import socket
import sys
import select

from parser import HTTPRequest
from response import MakeHTTPResponse
from psql import Database
from login import login


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
        self.psql = Database()
        self.psql.start()

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
        recv = conn.recv(1024)
        message = recv
        while not b'\r\n\r\n' in message:
            message += recv
            recv = conn.recv(1024)
#        print(request.decode())

        if message:
            request = HTTPRequest(message.decode())
            if request.path in self.paths.keys():
                json = self.paths[request.path](request, self.psql)
                makeResponse = MakeHTTPResponse(200, json)
            else:
                makeResponse = MakeHTTPResponse(404, '')
                
            response = makeResponse.make()
#            print(response.decode())
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
    port = 8081
    server = Server((ip, port))
    try:
        server.add_path('/login', login)
        server.start()
    except KeyboardInterrupt:
        sys.exit(0)
        
    


