from datetime import datetime

class Transaction:
    def __init__(self, amount, category, trans_type, date=None):
        self.amount = float(amount)
        self.category = category 
        self.type = trans_type.lower()
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "type": self.type,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        return Transaction(
            amount=data["amount"],
            category=data["category"],
            trans_type=data["type"],
            date=data["date"]
        )