package exercicio2;

public class Deposito {
    private int items = 0;
    private final int capacidade = 10;

    public synchronized void retirar() throws InterruptedException {
        if (items > 0) {
            items--;
            printar("Caixa retirada: Sobram " + items + " caixas");
            return;
        }
        printar("Sem caixas disponíveis, aguardando até uma nova caixa ser inserida");
        wait();
    }

    public synchronized void colocar() {
        if (items < capacidade) {
            items++;
            printar("Caixa armazenada: Passaram a ser " + items + " caixas");
        }
        notify();
    }

    private void printar(String msg) {
        System.out.println(msg + ". Thread: " + Thread.currentThread().getId());
    }

    public static void main(String[] args) {
        Deposito dep = new Deposito();

        new Thread(new Produtor(dep, 2)).start();
        new Thread(new Consumidor(dep, 1)).start();
        new Thread(new Consumidor(dep, 1)).start();


    }
}
