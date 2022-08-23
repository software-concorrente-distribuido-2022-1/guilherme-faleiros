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
    request = json.loads(data)
    age = request.get('age')
    name = request.get('name')
    gender = request.get('gender')

    if (gender == 'M' and age >= 18) or (gender == 'F' and age >= 21):
        return json.dumps({ 'name': name, 'maiority': True})
    return json.dumps({ 'name': name, 'maiority': False })



server = BaseServer(3000, 1024, handler)
server.start_server()