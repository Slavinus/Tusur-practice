class Account:
    def __init__(self, number, owner, balance=0):
        self.number = number
        self.owner = owner
        self.balance = balance
        if self.balance < 0:
            raise ValueError("Баланс не может быть отрицательным")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Пополнение не может быть отрицательным")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        if amount <= 0:
            raise ValueError("Так нельзя")
        self.balance -= amount
        return self.balance

    def __repr__(self):
        return f"Account({self.number!r}, {self.owner!r}, {self.balance})"