from xmlrpc.server import SimpleXMLRPCServer
import json

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

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(handler, "consume")
server.serve_forever()