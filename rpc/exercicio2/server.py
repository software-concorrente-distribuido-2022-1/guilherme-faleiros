from xmlrpc.server import SimpleXMLRPCServer
import json

OPR_FEE = 0.18
DVLP_FEE = 0.20

def handler(data):
    request = json.loads(data)
    age = request.get('age')
    name = request.get('name')
    gender = request.get('gender')

    if (gender == 'M' and age >= 18) or (gender == 'F' and age >= 21):
        return json.dumps({ 'name': name, 'maiority': True})
    return json.dumps({ 'name': name, 'maiority': False })

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(handler, "consume")
server.serve_forever()