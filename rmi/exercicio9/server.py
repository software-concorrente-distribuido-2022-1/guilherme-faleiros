import Pyro4

import random

@Pyro4.expose
class Card:
        
    def get_description(self, value, naipe):
        return f"{self.get_value(value)} de {self.get_naipe(naipe)}"

    def get_value(self, value):
        if value == 1:
            return 'Ás'
        if value == 11:
            return 'Valete'
        if value == 12:
            return 'Rainha'
        if value == 13:
            return 'Rei'
        return value
    
    def get_naipe(self, naipe):
        if naipe == 1:
            return 'ouros'
        elif naipe == 2:
            return 'paus'
        elif naipe == 3:
            return 'copas'
        elif naipe == 4:
            return 'espadas'

    def handle(self, data):
        print('Entrou aqui')
        desc = self.get_description(random.randint(1, 14), random.randint(1, 5))
        print(desc)
        return desc

Pyro4.Daemon.serveSimple({
    Card: 'Server',
}, host="0.0.0.0", port=9090, ns=False, verbose=True) 