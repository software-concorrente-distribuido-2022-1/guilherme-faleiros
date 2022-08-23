package question3;

public class Main {

    public static void main(String[] args) {
        var account = new Account(100l);
        new DepositOperation(account, 1000l).start();
        new UpdateOperation(account, 0.1).start();
    }
}
