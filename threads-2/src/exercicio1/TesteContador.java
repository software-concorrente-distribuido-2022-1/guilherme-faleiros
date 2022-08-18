package exercicio1;

public class TesteContador {

    public static void main(String[] args) {
        var runnable1 = new Contador();
        var runnable2 = new Contador();

        new Thread(runnable1).start();
        new Thread(runnable2).start();
    }
}
