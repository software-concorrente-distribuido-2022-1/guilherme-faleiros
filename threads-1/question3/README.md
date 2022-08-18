Esta é uma situação possível? Qual sua sugestão para contornar este problema?

Resposta: É sim uma situação possível. A principal solução que consequi achar, foi utilizando o modificador synchronized do
java nos métodos de depositar e atualizar para que se uma thread iniciar uma operação com este método, ela não seja 
interrompida até seu término, de modo que o saldo não tenha incosistências ao final da execução das duas threads/operações.