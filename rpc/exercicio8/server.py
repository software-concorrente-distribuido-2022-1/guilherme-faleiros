from xmlrpc.server import SimpleXMLRPCServer
import json

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

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(handler, "consume")
server.serve_forever()