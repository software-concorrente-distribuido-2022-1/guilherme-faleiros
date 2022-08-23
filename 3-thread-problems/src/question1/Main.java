package question1;


public class Main {

    public static void main(String[] args) throws InterruptedException {
        var counterThread = new Counter();
        counterThread.start();
        counterThread.join();
        System.out.println("Programa finalizado");
    }

}
