import csv

# Filter clothing by price and stock
def filter_clothing(filename):
    with open(filename, 'r') as file:
        reader = list(csv.DictReader(file))
        i = 0
        while i < len(reader):
            row = reader[i]
            if float(row['Price']) < 60 and int(row['Stock_Quantity']) < 40:
                print(f"{row['Product_Name']}: Price: {row['Price']}, Stock_Quantity: {row['Stock_Quantity']}")
            i += 1
filter_clothing('FileHandling\\PracticeMakesPerfect\\clothing.csv')
