import Pyro4
import json

@Pyro4.expose
class Server:
        
    def handle(self, data):
        def response(can_retire):
            return json.dumps({ 'can_retire': can_retire })

        request = json.loads(data)
        job_years = request.get('job_years')
        age = request.get('age')

        if (age >= 65) and (job_years >= 30) and ((age >= 60) and (job_years >= 25)):
            return response(True)
        else:
            return response(False)

Pyro4.Daemon.serveSimple({
    Server: 'Server',
}, host="0.0.0.0", port=9090, ns=False, verbose=True) 