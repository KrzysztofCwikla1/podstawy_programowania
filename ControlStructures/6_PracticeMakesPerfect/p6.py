enter_money = int(input("Choose amount of hours (1-2h), (3-6h), (>6h) =>"))

counter = 0

if enter_money >=1 and enter_money <=2:
    counter += 5
elif enter_money >= 3 and enter_money <=6:
    counter += 15
elif enter_money > 6:
    counter += 20

print(f"{counter} PLN")
