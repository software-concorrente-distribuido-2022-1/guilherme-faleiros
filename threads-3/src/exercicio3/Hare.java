package exercicio3;

import java.util.Random;

public class Hare extends Thread {

    private final Integer hareId;
    private final Race race;
    private Integer totalSteps = 0;

    public Hare(final Integer id, final Race race) {
        this.hareId = id;
        this.race = race;
    }

    public Integer getHareId() {
        return hareId;
    }

    public Integer getTotalSteps() {
        return totalSteps;
    }

    @Override
    public void run() {
        int meters = 0;
        while (meters < 20) {
            int jump = new Random().nextInt(3) + 1;
            meters += jump;
            this.totalSteps++;
            System.out.println("Lebre " + hareId + " pulou " + jump + " metros");
            yield();
        }
        race.finish(this);
    }

}
