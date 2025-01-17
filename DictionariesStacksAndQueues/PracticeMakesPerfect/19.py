import json

# Load the reservation data from the JSON file
def load_reservations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['reservations']

# Calculate the total number of rooms (reservations)
def total_rooms(reservations):
    return len(reservations)

# Calculate the number of paid reservations
def paid_reservations(reservations):
    return len([reservation for reservation in reservations if reservation['paid']])

# Calculate the number of unpaid reservations
def unpaid_reservations(reservations):
    return len([reservation for reservation in reservations if not reservation['paid']])

# Calculate the total value of paid reservations
def total_paid_value(reservations):
    return sum(reservation['nights'] * reservation['price_per_night'] for reservation in reservations if reservation['paid'])

# Calculate the total value of unpaid reservations
def total_unpaid_value(reservations):
    return sum(reservation['nights'] * reservation['price_per_night'] for reservation in reservations if not reservation['paid'])

# Print the summary information
def print_summary(reservations):
    print("Number of rooms:", total_rooms(reservations))
    print("Number of paid reservations:", paid_reservations(reservations))
    print("Number of unpaid reservations:", unpaid_reservations(reservations))
    print("Total value of paid reservations: $", total_paid_value(reservations))
    print("Total value of unpaid reservations: $", total_unpaid_value(reservations))

# Main program
def main():
    reservations = load_reservations('reservations.json')
    print_summary(reservations)

# Run the program
if __name__ == "__main__":
    main()
