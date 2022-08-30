import xmlrpc.client
import json

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

message = proxy.consume(json.dumps({ 'age': 19, 'name': 'Guilherme', 'gender': 'M'}))
print(message)
message = proxy.consume(json.dumps({ 'age': 19, 'name': 'Karine', 'gender': 'F'}))
print(message)
message = proxy.consume(json.dumps({ 'age': 17, 'name': 'Caio', 'gender': 'F'}))
print(message)
message = proxy.consume(json.dumps({ 'age': 21, 'name': 'Sofia', 'gender': 'F'}))
print(message)
