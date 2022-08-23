package exercicio1;

public class Tela{
    // Recurso disputado

    String texto;
    public synchronized void setTexto(String s) throws InterruptedException {
        texto = s;
        wait();
    }

    public synchronized void mostraTexto( ){
        System.out.println(texto);
        notifyAll();
    }
}
