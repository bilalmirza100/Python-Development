class BudgetAlert:
    @staticmethod
    def check_alert(user):
        total_income = user.get_total_income()
        total_expense = user.get_total_expense()

        if total_income == 0:
            return

        percentage_used = (total_expense / total_income) * 100

        if percentage_used >= 80:
            print("\n" + "!" * 50)
            print(f"⚠️  WARNING ALERT: You have spend {percentage_used:.1f}% from your money!")
            print(f"💰 Remaining Balance: PKR {user.get_balance():,.2f}")
            print("!" * 50 + "\n")