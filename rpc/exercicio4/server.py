from xmlrpc.server import SimpleXMLRPCServer
import json

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

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(handler, "consume")
server.serve_forever()