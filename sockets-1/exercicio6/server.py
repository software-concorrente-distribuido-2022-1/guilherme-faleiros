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
    def response(liquid_salary, name, level):
        return json.dumps({ 'liquid_salary': liquid_salary, 'name': name, 'level': level})

    request = json.loads(data)
    name = request.get('name')
    level = request.get('level')
    dependents = request.get('dependents')
    salary = request.get('salary')

    fee = 0
    if level == 'A':
        fee = 0.08 if dependents > 0 else 0.03
    if level == 'B':
        fee = 0.10 if dependents > 0 else 0.05
    if level == 'C':
        fee = 0.15 if dependents > 0 else 0.08
    if level == 'D':
        fee = 0.17 if dependents > 0 else 0.10
    
    return response(salary - (salary * fee), name, level)





server = BaseServer(3000, 1024, handler)
server.start_server()