countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "USA", "population": 331000000},
    {"name": "India", "population": 1390000000},
    {"name": "Germany", "population": 83000000},
    {"name": "Canada", "population": 38000000}
]

print("COUNTRY  POPULATION")
for country in countries:
    print(f"{country['name']:8} {country['population']}")