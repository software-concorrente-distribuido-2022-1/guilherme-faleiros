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
    def response(can_retire):
        return json.dumps({ 'can_retire': can_retire })

    request = json.loads(data)
    job_years = request.get('job_years')
    age = request.get('age')

    if (age >= 65) and (job_years >= 30) and ((age >= 60) and (job_years >= 25)):
        return response(True)
    else:
        return response(False)

server = BaseServer(3000, 1024, handler)
server.start_server()