import socket
import json
from threading import Thread

BACKLOG = 5

class BaseServer:

    def __init__(self, port, max_size, box):
        self.port = port
        self.max_size = max_size
        self.box = box
    
    def start_server(self):
        host = 'localhost'

        server_socket = socket.socket()
        server_socket.bind((host, self.port))

        print(f"Server started on port {self.port}")

        server_socket.listen(BACKLOG)

        while True:
            connection, address = server_socket.accept()
            t = Thread(target=self.new_client, args=(connection, address))
            t.setDaemon(True)
            t.start()

    def new_client(self, connection, address):
        while True:
            print(f"Incoming request from host {address}")
            data = connection.recv(self.max_size).decode()
            if not data:
                break
            message = self.box.handle_request(data)
            connection.send(message.encode())

        connection.close()