class MakeHTTPResponse:
    def __init__(self, status, json):
        self.status = int(status)
        self.json = json

        self.statusResponse = {200: 'OK', 201: 'Created', 204: 'No content',\
            401: 'Unauthorized', 403: 'Forbidden', 404: 'Not found', }
        self.httpVersion = 'HTTP/1.1'
        self.content_type = 'Content-Type: application/json'
        self.charset = 'charset=utf-8'
        self.length = str(len(json))
        self.contentLength = f'content-length: {self.length}'
        
    def make(self):
        header = f'{self.httpVersion} {self.status} {self.statusResponse[self.status]}'
        addInfo = f'{self.content_type}; {self.charset}'

        response = f'{header}\r\n{addInfo}\r\n{self.contentLength}\r\n\r\n{self.json}'
        
        return response.encode()

