package question1;

public class Counter extends Thread{
    @Override
    public void run() {
        for (int i = 1; i < 101; i++) {
            System.out.println(i);
        }
    }
}
