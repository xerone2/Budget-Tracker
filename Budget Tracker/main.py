import json
import matplotlib.pyplot as plt

def load_transactions():
    try:
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = {'income': [], 'expenses': []}
    return transactions

def save_transactions(transactions):
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file, indent=2)

def record_transaction(transactions, transaction_type, category, amount):
    transactions[transaction_type].append({'category': category, 'amount': amount})
    save_transactions(transactions)

def calculate_remaining_budget(transactions):
    income = sum(item['amount'] for item in transactions['income'])
    expenses = sum(item['amount'] for item in transactions['expenses'])
    remaining_budget = income - expenses
    return remaining_budget

def display_spending_trends(transactions):
    expense_categories = [item['category'] for item in transactions['expenses']]
    expense_amounts = [item['amount'] for item in transactions['expenses']]

    plt.pie(expense_amounts, labels=expense_categories, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Spending Trends')
    plt.show()

def main():
    transactions = load_transactions()

    while True:
        print("\n1. Record Income")
        print("2. Record Expense")
        print("3. Calculate Remaining Budget")
        print("4. Display Spending Trends")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            record_transaction(transactions, 'income', category, amount)

        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            record_transaction(transactions, 'expenses', category, amount)

        elif choice == '3':
            remaining_budget = calculate_remaining_budget(transactions)
            print(f"Remaining Budget: ${remaining_budget:.2f}")

        elif choice == '4':
            display_spending_trends(transactions)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
