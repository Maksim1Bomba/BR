class MakeHTTPResponse:
    def __init__(self, status, json):
        self.status = int(status)
        self.json = json

        self.statusResponse = {200: 'OK', 404: 'Not found'}
        self.httpVersion = 'HTTP/1.1'
        self.content_type = 'Content-Type: application/json'
        self.charset = 'charset=utf-8'
        self.length = str(len(json))
        
    def make(self):
        header = f'{self.httpVersion} {self.status} {self.statusResponse[self.status]}'
        addInfo = f'{self.content_type}; {self.charset}'

        response = f'{header}\r\n{addInfo}\r\n\r\n{self.json}'
        
        return response.encode()


a = MakeHTTPResponse(200, '{asas: asdas}')
print(a.make().decode())

