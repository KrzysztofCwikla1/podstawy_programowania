categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
max_expense = max(expenses)
most_expensive_category = categories[expenses.index(max_expense)]

print(f'The most expensive category is: {most_expensive_category}')