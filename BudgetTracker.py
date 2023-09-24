#Budget Tracker
class BudgetTracker:
    def __init__(self):
        self.expenses = []
        self.income = []
        self.savings = 0

    def add_expense(self, amount, category):
        self.expenses.append({"amount": amount, "category": category})

    def add_income(self, amount, category):
        self.income.append({"amount": amount, "category": category})

    def calculate_total_expenses(self):
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        return total_expenses

    def calculate_total_income(self):
        total_income = sum(income["amount"] for income in self.income)
        return total_income

    def calculate_total_savings(self):
        total_savings = self.calculate_total_income() - self.calculate_total_expenses()
        self.savings = total_savings
        return total_savings


def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\nBudget Tracker")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. Calculate Savings")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            budget_tracker.add_expense(amount, category)
            print("Expense added successfully.")
        elif choice == '2':
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            budget_tracker.add_income(amount, category)
            print("Income added successfully.")
        elif choice == '3':
            total_savings = budget_tracker.calculate_total_savings()
            print("Total Savings:", total_savings)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()