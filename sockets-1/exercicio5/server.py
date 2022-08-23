import json
import socket
from threading import Thread

BACKLOG = 5

class BaseServer:

    def __init__(self, port, max_size, handler):
        self.port = port
        self.max_size = max_size
        self.handler = handler
    
    def start_server(self):
        host = 'localhost'

        server_socket = socket.socket()
        server_socket.bind((host, self.port))

        print(f"Server started on port {self.port}")

        server_socket.listen(BACKLOG)

        while True:
            connection, address = server_socket.accept()
            self.new_client(connection, address)

    def new_client(self, connection, address):
        while True:
            print(f"Incoming request from host {address}")
            data = connection.recv(self.max_size).decode()
            if not data:
                break
            message = self.handler(data)
            connection.send(message.encode())

        connection.close()

def handler(data):
    def response(category):
        return json.dumps({ 'category': category})

    request = json.loads(data)
    age = request.get('age')

    print(age)

    if age >= 5 and age <= 7:
        return response('infantil A')
    elif age >= 8 and age <= 10:
        return response('infantil B')
    elif age >= 11 and age <= 13:
        return response('juvenil A')
    elif age >= 14 and age <= 17:
        return response('juvenil B')
    elif age >= 18:
        return response('adulto')

server = BaseServer(3000, 1024, handler)
server.start_server()