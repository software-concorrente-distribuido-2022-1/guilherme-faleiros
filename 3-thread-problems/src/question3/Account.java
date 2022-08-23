package question3;

import java.math.BigDecimal;

public class Account {
    private double balance;

    public Account() {
        this.balance = 0l;
    }

    public Account(final double balance) {
        this.balance = balance;
    }

    public synchronized void update(final double fee) {
        var newValue = this.balance * (1 + fee);
        this.balance = newValue;
        System.out.println("New value after update: " + this.balance);
    }

    public synchronized void deposit(final double amount) {
        this.balance = this.balance + amount;
        System.out.println("New value after deposit: " + this.balance);
    }
}
