package exercicio3;

import java.util.ArrayList;
import java.util.List;

public class Race {
    private List<Hare> hares = new ArrayList<>();

    public synchronized void finish(Hare lebre) {
        this.hares.add(lebre);
    }

    public List<Hare> getHares() {
        return hares;
    }

    public static void main(String[] args) throws InterruptedException {
        Race race = new Race();

        var t1 = new Hare(1, race);
        var t2= new Hare(2, race);
        var t3 = new Hare(3, race);
        var t4 = new Hare(4, race);
        var t5= new Hare(5, race);

        t1.start();
        t2.start();
        t3.start();
        t4.start();
        t5.start();

        t1.join();
        t2.join();
        t3.join();
        t4.join();
        t5.join();

        var count = 1;
        System.out.println("VENCEDORA: Lebre " + race.getHares().get(0).getHareId());
        System.out.println("------------ COLOCAÇÃO -------------");
        for (var hare : race.getHares()) {
            System.out.println(count + "o lugar: Lebre " + hare.getHareId() + ". Quantidade de passos: " + hare.getTotalSteps());
            count++;
        }

    }


}
