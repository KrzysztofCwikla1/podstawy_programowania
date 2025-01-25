names = ['James', 'Emily', 'William', 'Olivia', 'Benjamin', 'Sophia', 'Henry']

# Sort names by length using anonymous function
sorted_names = sorted(names, key=lambda name: len(name))

# Print sorted list
for name in sorted_names:
    print(name)
