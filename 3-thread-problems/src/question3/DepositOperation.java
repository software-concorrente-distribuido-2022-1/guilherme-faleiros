package question3;

public class DepositOperation extends Thread {
    private final Account account;
    private final double amount;

    public DepositOperation(final Account account, final double amount) {
        this.account = account;
        this.amount = amount;
    }

    @Override
    public void run() {
        account.deposit(amount);
    }
}
