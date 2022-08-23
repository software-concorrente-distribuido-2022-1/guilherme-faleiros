package exercicio1;

public class UserSemControle extends Thread{
    private Tela recurso; // Recurso disputado, sem proteção de acesso
    private String nomeThread; // Identificacao da thread
    public UserSemControle(String str,Tela r) {
        recurso = r;
        nomeThread = str;
    }

    public void run( ) {
        for (int i=0; i<5; i++) {
            try {
                recurso.setTexto(nomeThread); // Seta recurso compartilhado
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            try{
                sleep(30);
            } catch(Exception e){ }
            recurso.mostraTexto(); // Usa recurso compartilhado
        }
    }
}
