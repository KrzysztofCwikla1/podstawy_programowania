# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

# Calculate total seats
def seats_total(seats):
    return len(seats) * len(seats[0])

# Calculate available seats
def seats_available(seats):
    available = 0
    for row in seats:
        available += row.count('A')
    return available

# Calculate booked seats
def seats_booked(seats):
    booked = 0
    for row in seats:
        booked += row.count('B')
    return booked

# Check the status of a specific seat
def seat_status(seats, row, place):
    if row < 1 or row > len(seats) or place < 1 or place > len(seats[0]):
        return "Invalid seat location"
    return "Available" if seats[row - 1][place - 1] == 'A' else "Booked"

# Print cinema information table
print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))
