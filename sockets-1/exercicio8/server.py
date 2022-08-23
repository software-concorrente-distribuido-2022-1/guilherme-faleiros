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
    def response(fee, value):
        return json.dumps({ 'fee': fee, 'credit_value': value * fee })

    request = json.loads(data)
    medium_balance = request.get('medium_balance')

    if medium_balance >= 0 and medium_balance <= 200:
        return response(0.0, medium_balance)
    if medium_balance >= 201 and medium_balance <= 400:
        return response(0.2, medium_balance)
    if medium_balance >= 401 and medium_balance <= 600:
        return response(0.3, medium_balance)
    if medium_balance > 600:
        return response(0.4, medium_balance)

server = BaseServer(3000, 1024, handler)
server.start_server()