from p3cl1 import Transaction

class User:
    def __init__(self, name):
        self.name = name
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_total_income(self):
        return sum(t.amount for t in self.transactions if t.type == 'income')

    def get_total_expense(self):
        return sum(t.amount for t in self.transactions if t.type == 'expense')

    def get_balance(self):
        return self.get_total_income() - self.get_total_expense()