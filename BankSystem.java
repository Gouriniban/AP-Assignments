import java.util.*;

// Base Class
class Account {
    private String accountNumber;
    private String ownerName;
    private double balance;

    // Default constructor (constructor chaining)
    public Account() {
        this("0000", "Unknown", 0.0);
    }

    // Parameterized constructor
    public Account(String accountNumber, String ownerName, double balance) {
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        setBalance(balance);
    }

    // Getters
    public String getAccountNumber() {
        return accountNumber;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public double getBalance() {
        return balance;
    }

    // Setters
    public void setAccountNumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }

    public void setOwnerName(String ownerName) {
        this.ownerName = ownerName;
    }

    public void setBalance(double balance) {
        if (balance < 0) {
            throw new IllegalArgumentException("Balance cannot be negative");
        }
        this.balance = balance;
    }

    // Deposit method
    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit must be positive");
        }
        balance += amount;
    }

    // Withdraw method
    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal must be positive");
        }
        if (amount > balance) {
            throw new IllegalArgumentException("Insufficient balance");
        }
        balance -= amount;
    }

    // Display method
    public void display() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Owner Name: " + ownerName);
        System.out.println("Balance: " + balance);
    }
}

// SavingsAccount Class
class SavingsAccount extends Account {
    private double interestRate;

    public SavingsAccount() {
        this("0000", "Unknown", 0.0, 0.0);
    }

    public SavingsAccount(String accNo, String owner, double balance, double interestRate) {
        super(accNo, owner, balance);
        this.interestRate = interestRate;
    }

    public double getInterestRate() {
        return interestRate;
    }

    public void setInterestRate(double rate) {
        if (rate < 0) {
            throw new IllegalArgumentException("Interest rate cannot be negative");
        }
        this.interestRate = rate;
    }

    public double calculateInterest() {
        return getBalance() * interestRate / 100;
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Interest Rate: " + interestRate + "%");
        System.out.println("Interest: " + calculateInterest());
        System.out.println("-------------------------");
    }
}

// CurrentAccount Class
class CurrentAccount extends Account {
    private double overdraftLimit;

    public CurrentAccount() {
        this("0000", "Unknown", 0.0, 0.0);
    }

    public CurrentAccount(String accNo, String owner, double balance, double overdraftLimit) {
        super(accNo, owner, balance);
        this.overdraftLimit = overdraftLimit;
    }

    public double getOverdraftLimit() {
        return overdraftLimit;
    }

    public void setOverdraftLimit(double limit) {
        if (limit < 0) {
            throw new IllegalArgumentException("Overdraft cannot be negative");
        }
        this.overdraftLimit = limit;
    }

    @Override
    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal must be positive");
        }

        if (amount > getBalance() + overdraftLimit) {
            throw new IllegalArgumentException("Overdraft limit exceeded");
        }

        // Allow overdraft
        double newBalance = getBalance() - amount;

        if (newBalance < 0) {
            System.out.println("Using overdraft facility...");
            newBalance = 0;
        }

        setBalance(newBalance);
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Overdraft Limit: " + overdraftLimit);
        System.out.println("-------------------------");
    }
}

// Main Class
public class BankSystem {
    public static void main(String[] args) {

        List<Account> accounts = new ArrayList<>();

        // Polymorphism
        accounts.add(new SavingsAccount("S101", "Gouriniban", 5000, 5));
        accounts.add(new CurrentAccount("C201", "Rahul", 2000, 1000));

        for (Account acc : accounts) {
            try {
                acc.deposit(1000);
                acc.withdraw(3000);
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
            }

            acc.display();
        }
    }
}
