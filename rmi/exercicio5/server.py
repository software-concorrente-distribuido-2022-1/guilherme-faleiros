import Pyro4
import json

@Pyro4.expose
class Server:
        
    def handle(self, data):
        def response(category):
            return json.dumps({ 'category': category})

        request = json.loads(data)
        age = request.get('age')

        print(age)

        if age >= 5 and age <= 7:
            return response('infantil A')
        elif age >= 8 and age <= 10:
            return response('infantil B')
        elif age >= 11 and age <= 13:
            return response('juvenil A')
        elif age >= 14 and age <= 17:
            return response('juvenil B')
        elif age >= 18:
            return response('adulto')

Pyro4.Daemon.serveSimple({
    Server: 'Server',
}, host="0.0.0.0", port=9090, ns=False, verbose=True) 