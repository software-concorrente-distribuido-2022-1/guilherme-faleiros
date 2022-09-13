import Pyro4

import json

ipAddressServer = "0.0.0.0"

server = Pyro4.core.Proxy('PYRO:Server@' + ipAddressServer + ':9090')
print(server.handle(json.dumps({ 'job_years': 20, 'age': 40 })))
print(server.handle(json.dumps({ 'job_years': 30, 'age': 65 })))