medal_data = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
]

# Filter countries that have at least 10 medals
countries_with_10_medals = filter(lambda x: x["gold"] + x["silver"] + x["bronze"] >= 10, medal_data)

for country in countries_with_10_medals:
    print(f"{country['country']}: {country['gold']},{country['silver']},{country['bronze']}")
