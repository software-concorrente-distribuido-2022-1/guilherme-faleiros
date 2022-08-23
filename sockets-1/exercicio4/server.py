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
    def response_weight(weight):
        return json.dumps({ 'weight': weight})

    def woman(height):
        return response_weight((72.7 * height) - 58)

    def man(height):
        return response_weight((62.1 * height) - 44.7)


    request = json.loads(data)
    height = request.get('height')
    gender = request.get('gender')

    if gender == 'M':
        return man(height)
    elif gender == 'F':
        return woman(height)



server = BaseServer(3000, 1024, handler)
server.start_server()