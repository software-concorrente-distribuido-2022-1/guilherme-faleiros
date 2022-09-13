import Pyro4
import json

OPR_FEE = 0.18
DVLP_FEE = 0.20

@Pyro4.expose
class Server:
        
    def handle(self, data):
        request = json.loads(data)

        def new_salary(request, fee):
            return request.get('salary') + (request.get('salary') * fee)

        if request.get('role') == 'OPR':
            return json.dumps({ 'new_salary': new_salary(request, OPR_FEE), 'name': request.get('name') })
        elif request.get('role') == 'DVLP':
            return json.dumps({ 'new_salary': new_salary(request, DVLP_FEE), 'name': request.get('name') })

Pyro4.Daemon.serveSimple({
    Server: 'Server',
}, host="0.0.0.0", port=9090, ns=False, verbose=True) 