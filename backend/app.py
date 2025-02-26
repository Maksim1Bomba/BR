import socket
import sys
import selectors
import types

from parser2 import HTTPResponseParse

class Server:
    def __init__(self, server_addr):
        self.server_addr = server_addr
        self.sel = selectors.DefaultSelector()

    def decode_http(self, st):
        return json.loads(st)
        

    def start(self):
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock.bind(self.server_addr)
        self.lsock.listen()
        print(f"Listening on {self.server_addr}")
        self.lsock.setblocking(False)
        self.sel.register(self.lsock, selectors.EVENT_READ, data=None)

    def accept_wrapper(self, sock):
        conn, addr = sock.accept()
        print(f"Accepted connection from {addr}")
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(conn, events, data=data)

    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data

        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                data.outb += recv_data
            else:
                print(f"Closing connection to {data.addr}")
                self.sel.unregister(sock)
                sock.close()
                
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print(data.outb)
                request = HTTPResponseParse(data.outb)
                sent = sock.send(request.parse_request().decode())
                data.outb = data.outb[sent:]
            
            
    def work(self):
        try:
            while True:
                event = self.sel.select(timeout=None)
                for key, mask in event:
                    if key.data is None:
                        self.accept_wrapper(key.fileobj)
                    else:
                        self.service_connection(key, mask)
        except KeyboardInterrupt:
            self.sel.close()
            
if __name__ == "__main__":
    server = Server(('127.0.0.1', 8082))
    try:
        server.start()
        server.work()
    except KeyboardInterrupt:
        sys.exit(0)
        
    
