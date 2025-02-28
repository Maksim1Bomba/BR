import socket
import sys
import threading

from parser2 import HTTPRequest

class Server:
    def __init__(self, server_addr):
        self.server_addr = server_addr
    
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
        while not '\r\n' in data and not '\n\n' in data:
            out = conn.recv(1024)
            if not out:
                connected = False
                break
            else:
                data += out.decode()

        print(data)
            
        while connected:
            request = HTTPRequest(data)
            response = b"HTTP/1.1 404 Bad request\r\nContent-Length: 9\r\n\r\nNot found"
            print(response.decode())
            while not response:
                sent = conn.send(response)
                response = response[sent:]
            connected = False
        print(f"Close connection on {addr}")
        conn.close()
        
            
                
                

if __name__ == "__main__":
    ip = str(sys.argv[1])
    port = int(sys.argv[2])
    server = Server((ip, port))
    try:
        server.start()
    except KeyboardInterrupt:
        sys.exit(0)
        
    
