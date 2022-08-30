import xmlrpc.client
import json

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

message = proxy.consume(json.dumps({ 'medium_balance': 2031.31}))
print(message)