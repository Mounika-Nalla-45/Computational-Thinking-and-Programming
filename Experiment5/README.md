## 5. Banking Management System Using Inheritance and Abstraction

### Aim

To develop a banking management system demonstrating Inheritance and
Abstraction with full Type Hints using Python.

### Algorithm

1.  Create an abstract `BankAccount` class.
2.  Define deposit and withdrawal operations.
3.  Create a `SavingsAccount` subclass using inheritance.
4.  Implement the withdrawal method.
5.  Perform deposit and withdrawal operations.
6.  Display the account balance.

### Python Program

``` python
from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, balance: float) -> None:
        self.balance: float = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass


class SavingsAccount(BankAccount):
    def withdraw(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")


account: BankAccount = SavingsAccount(1000.0)

account.deposit(500.0)
account.withdraw(200.0)

print("Balance:", account.balance)
```

### Data (Input)

``` text
Initial balance: 1000
Deposit: 500
Withdrawal: 200
Account type: Savings Account
```

### Result (Output)

``` text
Balance: 1300.0
```

### Inference

Inheritance and Abstraction help create a reusable and organized banking
system.

### Analysis

-   Time complexity: `O(1)` for deposit and withdrawal.
-   Space complexity: `O(1)` for the stored account balance.
-   Inheritance: `SavingsAccount` inherits from `BankAccount`.
-   Abstraction: `BankAccount` defines the abstract `withdraw()` method.
