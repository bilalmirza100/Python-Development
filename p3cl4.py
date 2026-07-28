import json
import os
from p3cl1 import Transaction
from p3cl2 import User
from p3cl3 import BudgetAlert

class FinanceManager:
    def __init__(self, user_name, filename="finance_data.json"):
        self.filename = filename
        self.user = User(user_name)
        self.load_from_file()

    def add_transaction(self, amount, category, trans_type):
        t = Transaction(amount, category, trans_type)
        self.user.add_transaction(t)
        self.save_to_file()
        print(f"\n✅ SUCCESS: {trans_type.capitalize()} of PKR {amount} added successfully!")

        BudgetAlert.check_alert(self.user)

    def save_to_file(self):
        data = {
            "user_name": self.user.name,
            "transactions": [t.to_dict() for t in self.user.transactions]
        }
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    for t_data in data.get("transactions", []):
                        self.user.add_transaction(Transaction.from_dict(t_data))
            except (json.JSONDecodeError, KeyError):
                print("⚠️ File corrupted ya empty hai, naye siray se shuru kar rahe hain.")

    def generate_report(self):
        income = self.user.get_total_income()
        expense = self.user.get_total_expense()
        balance = self.user.get_balance()

        print("\n" + "=" * 55)
        print(f"📊 FINANCIAL SUMMARY REPORT — {self.user.name.upper()}")
        print("=" * 55)
        print(f"🟢 Total Income  : PKR {income:,.2f}")
        print(f"🔴 Total Expense : PKR {expense:,.2f}")
        print(f"💵 Net Balance   : PKR {balance:,.2f}")
        print("-" * 55)
        print("DATE & TIME           | TYPE    | CATEGORY   | AMOUNT")
        print("-" * 55)

        if not self.user.transactions:
            print("         No transactions recorded yet.")
        else:
            for t in self.user.transactions:
                t_type = "INCOME " if t.type == "income" else "EXPENSE"
                print(f"{t.date} | {t_type} | {t.category:<10} | PKR {t.amount:,.2f}")
        
        print("=" * 55 + "\n")