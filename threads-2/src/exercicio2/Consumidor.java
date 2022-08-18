package exercicio2;

public class Consumidor implements Runnable {
    private final Integer intervalo;
    private final Deposito deposito;

    public Consumidor(final Deposito deposito, final Integer intervalo) {
        this.deposito = deposito;
        this.intervalo = intervalo;
    }

    private void printar(String msg) {
        System.out.println(msg + ". Thread: " + Thread.currentThread().getId());
    }

    @Override
    public void run() {
        while(true) {
            try {
                printar("Iniciando operação retirar()");
                deposito.retirar();
                printar("Iniciando intervalo de: " + this.intervalo + " segundos");
                Thread.sleep(this.intervalo * 1000);
            } catch (InterruptedException e) {
                printar("Falha ao realizar sleep");
                e.printStackTrace();
            }
        }
    }
}
