categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
max_expense = max(expenses)

print(f'The most expensive category is: {categories[expenses.index(max_expense)]}')