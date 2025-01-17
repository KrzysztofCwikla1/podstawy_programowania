# Function to get the list of hotel names
def hotel_list(hotels):
    return ", ".join([hotel['name'] for hotel in hotels])

# Function to calculate the average price of hotels
def avg_price(hotels):
    total_price = sum([hotel['price'] for hotel in hotels])
    return round(total_price / len(hotels))

# Hotels data for Krakow and Sopot
hotels_in_Krakow = [
   {"name":"Sky", "price":320.00},
   {"name":"Metropol", "price":480.00},
   {"name":"New Port", "price":420.00},
   {"name":"Aparthotel", "price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus", "price":510.00},
   {"name":"Aqua", "price":345.00},
   {"name":"La Boutique", "price":390.00},
   {"name":"Marina", "price":410.00}
]

# Calculate and display the results
krakow_hotels = hotel_list(hotels_in_Krakow)
krakow_avg_price = avg_price(hotels_in_Krakow)
sopot_hotels = hotel_list(hotels_in_Sopot)
sopot_avg_price = avg_price(hotels_in_Sopot)

# Compare prices and determine which city has cheaper hotels
cheaper_hotels_in = "Krakow" if krakow_avg_price < sopot_avg_price else "Sopot" if sopot_avg_price < krakow_avg_price else "Neither"

# Display the results
print(f"Hotels in Krakow: {krakow_hotels}")
print(f"Average hotel price in Krakow: {krakow_avg_price}")
print(f"Hotels in Sopot: {sopot_hotels}")
print(f"Average hotel price in Sopot: {sopot_avg_price}")
print(f"Cheaper hotels in: {cheaper_hotels_in}")
