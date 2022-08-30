import xmlrpc.client
import json

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

message = proxy.consume(json.dumps({ 'height': 1.80, 'gender': 'M'}))
print(message)

message = proxy.consume(json.dumps({ 'height': 1.80, 'gender': 'F'}))
print(message)