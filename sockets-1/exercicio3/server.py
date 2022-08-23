import json
import socket
from threading import Thread
import functools

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
    n1 = request.get('n1')
    n2 = request.get('n2')
    n3 = request.get('n3')

    def approved():
        return json.dumps({'approved': True})
    
    def disapproved():
        return json.dumps({'approved': False})

    def average(notes):
        return functools.reduce(lambda a, b: a+b, notes)/len(notes)

    first_avg = average([n1, n2])
    if first_avg >= 7.0:
        return approved()
    elif first_avg > 3.0 and first_avg < 7.0:
        new_average = average([n1, n2, n3])
        if new_average >= 5.0:
            return approved()
        return disapproved()
    else:
        return disapproved()

server = BaseServer(3001, 1024, handler)
server.start_server()