from p3cl4 import FinanceManager

def is_valid_number(self):
    cleaned = self.replace('.', '', 1)
    return cleaned.isdigit() and float(self) > 0

def main():
    print("-" * 32)
    print("PROFESSIONAL CLI FINANCE MANAGER")
    print("-" * 32)
    
    user_name = input("Enter Your Name :").strip() or "User"
    manager = FinanceManager(user_name)

    while True:
        print("\n- MAIN MENU -")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Financial Report")
        print("4. Exit")
        
        choice = input("Option Chunien (1-4): ").strip()

        if choice == "1":
            amount_input = input("Enter Amount (PKR): ").strip()
            if is_valid_number(amount_input):
                amount = float(amount_input)
                category = input("Category (e.g., Salary, Business, Bonus): ").strip() or "General"
                manager.add_transaction(amount, category, "income")
            else:
                print("❌ Invalid Amount! Please enter the correct amount.")

        elif choice == "2":
            amount_input = input("Enter Amount (PKR): ").strip()
            if is_valid_number(amount_input):
                amount = float(amount_input)
                category = input("Category (e.g., Food, Rent, Travel, Bills): ").strip() or "General"
                manager.add_transaction(amount, category, "expense")
            else:
                print("❌ Invalid Amount! Please enter the correct amount.")

        elif choice == "3":
            manager.generate_report()

        elif choice == "4":
            print("\nThanK You! Your Data is safe! 👋")
            break
        else:
            print("Wrong Option! Please select between 1 to 4.")

if __name__ == "__main__":
    main()