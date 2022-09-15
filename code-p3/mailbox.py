import json
import threading

from base_server import BaseServer

class Mailbox:
    def __init__(self):
        self.message = None
        self.can_produce = True
        self.can_consume = False
        self.monitor = threading.Condition()
    
    def handle_request(self, data: str):
        request = json.loads(data)
        event_type = request.get('event_type')
        message = request.get('message')
        id = request.get('id')
        print(event_type)
        return self.store_message(message, id) if event_type == 'PRODUCE' else self.retrieve_message(id)
    
    def store_message(self, message, id):
        with self.monitor: 

            if not self.can_produce:
                self.monitor.wait()

            if (self.message == None):
                print(f"Produtor {id} produziu a mensagem: {message}")
                self.message = message
                self.can_consume = True
            else:
                self.can_produce = False

            self.monitor.notify()

            return str(self.message)
    
    def retrieve_message(self, id):
        with self.monitor:

            if not self.can_consume:
                self.monitor.wait()

            result_message = ""
            if (self.message != None):
                print(f"Consumidor {id} consumiu a mensagem: {self.message}")
                result_message = self.message
                self.message = None
                self.can_produce = True
            
            if self.message == None:
                self.can_consume = False
            
            self.monitor.notify()

            return str(result_message)
            
deposit_box_server = BaseServer(3000, 1024, Mailbox())
deposit_box_server.start_server()