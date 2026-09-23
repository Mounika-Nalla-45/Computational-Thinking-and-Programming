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