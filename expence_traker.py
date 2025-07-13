import json

class ExpenseTracker:
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)
                self.income = data["income"]
                self.expenses = data["expenses"]
        except FileNotFoundError:
            self.income = 0
            self.expenses = []

    def add_income(self, amount):
        self.income += amount
        print(f"Income added: {amount}")

    def add_expense(self, name, amount):
        self.expenses.append({"name": name, "amount": amount})
        print(f"Expense added: {name} - {amount}")

    def show_summary(self):
        total_expense = sum(item["amount"] for item in self.expenses)
        balance = self.income - total_expense
        print(f"\nTotal Income: {self.income}")
        print(f"Total Expense: {total_expense}")
        print(f"Balance Left: {balance}")
        print("\nExpenses List:")
        for item in self.expenses:
            print(f"- {item['name']}: {item['amount']}")

    def save_data(self):
        data = {"income": self.income, "expenses": self.expenses}
        with open(self.file_name, "w") as file:
            json.dump(data, file)
        print("Data saved successfully! 💙")

# -------------------------------
# Run
tracker = ExpenseTracker("expenses.json")

while True:
    print("\n=== Expense Tracker Menu ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Summary")
    print("4. Exit")

    choice = input("Select option (1-4): ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        tracker.add_income(amount)

    elif choice == "2":
        name = input("Expense name: ")
        amount = float(input("Expense amount: "))
        tracker.add_expense(name, amount)

    elif choice == "3":
        tracker.show_summary()

    elif choice == "4":
        tracker.save_data()
        break

    else:
        print("Invalid option.")
