# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Initialize totals
category_totals = [0, 0, 0]  # [Food, Transport, Utilities]
weekly_totals = [0, 0, 0, 0]  # Totals for Week 1, Week 2, Week 3, Week 4
monthly_total = 0

# Calculate totals
for week_index, week in enumerate(monthly_expenses):
    weekly_total = 0
    for category_index, expense in enumerate(week):
        category_totals[category_index] += expense  # Add to category total
        weekly_total += expense  # Add to weekly total
    weekly_totals[week_index] = weekly_total  # Store weekly total
    monthly_total += weekly_total  # Add to monthly total

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', category_totals[0])
print('Transport:', category_totals[1])
print('Utilities:', category_totals[2])
print('Week 1:', weekly_totals[0])
print('Week 2:', weekly_totals[1])
print('Week 3:', weekly_totals[2])
print('Week 4:', weekly_totals[3])
print('---------------')
print('TOTAL:', monthly_total)
