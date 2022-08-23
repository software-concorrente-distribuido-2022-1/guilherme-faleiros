package question2;

public class FruitPrinter extends Thread {

    private final String fruitName;

    public FruitPrinter(final String fruitName) {
        this.fruitName = fruitName;
    }

    @Override
    public void run() {
        while (true) {
            try {
                System.out.println(this.fruitName);
                sleep(3000);
            } catch (InterruptedException e) {
                System.out.println("Error on thread execution");
                e.printStackTrace();
            }
        }
    }
}
