package exercicio2;

import java.util.List;

public class Finder extends Thread {
    private final Result result;
    private final List<Unit> numbers;
    private final int numberToFind;

    public Finder(final Result result, final List<Unit> numbers, final int numberToFind) {
        this.result = result;
        this.numbers = numbers;
        this.numberToFind = numberToFind;
    }

    @Override
    public void run() {
        for (Unit unit : numbers) {
            if (result.isCompleted()) {
                break;
            }
            if (unit.getNumber() == numberToFind) {
                System.out.println(currentThread().getName() + " achou");
                result.setWantedIndex(unit.getIndex());
                break;
            }
        }
    }

}
