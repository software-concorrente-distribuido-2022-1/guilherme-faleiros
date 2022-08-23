package question3;

public class UpdateOperation extends Thread {
    private final Account account;
    private final double fee;

    public UpdateOperation(final Account account, final double fee) {
        this.account = account;
        this.fee = fee;
    }

    @Override
    public void run() {
        account.update(fee);
    }
}
