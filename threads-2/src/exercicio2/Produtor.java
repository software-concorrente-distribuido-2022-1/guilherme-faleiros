package exercicio2;

public class Produtor implements Runnable {
    private final Integer intervalo;
    private final Deposito deposito;

    public Produtor(final Deposito deposito, final Integer intervalo) {
        this.deposito = deposito;
        this.intervalo = intervalo;
    }

    private void printar(String msg) {
        System.out.println(msg + ". Thread: " + Thread.currentThread().getId());
    }

    public void run() {
        while(true) {
            try {
                printar("Iniciando operação colocar()");
                deposito.colocar();
                printar("Iniciando intervalo de: " + this.intervalo + " segundos");
                Thread.sleep(this.intervalo * 1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
