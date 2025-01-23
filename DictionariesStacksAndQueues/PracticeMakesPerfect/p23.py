import requests
import json

# Step 1: Fetch the data from the NBP API for Euro exchange rates in JSON format
url = 'https://api.nbp.pl/api/exchangerates/rates/A/EUR/last/10/?format=json'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Print the full response to inspect its structure
    # print(json.dumps(data, indent=4, ensure_ascii=False))  # Uncomment if you want to see the full response
    
    # Save the data to euro.json
    with open('euro.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    # Step 2: Display the exchange rates from the saved euro.json file
    with open('euro.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Print the header
    print("Date            Buying Rate     Selling Rate")
    print("============================================")
    
    # Step 3: Display the data in the required format
    for rate in data['rates']:
        date = rate['effectiveDate']
        # Since there's no 'bid' and 'ask', using 'mid' for both buying and selling rates
        buying_rate = rate['mid']
        selling_rate = rate['mid']
        
        # Print the data in the required format
        print(f"{date}      {buying_rate:<10}  {selling_rate}")
else:
    print("Failed to fetch data from NBP API.")
