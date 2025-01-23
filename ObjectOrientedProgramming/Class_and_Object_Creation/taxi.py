class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    def print_receipt(self):
        print(f"Distance: {self.distance} km")
        print(f"Rate: €{self.rate_per_km} per km")
        print(f"Fare: €{self.fare:.2f}")


def main():
# First taxi ride
    ride1 = TaxiRide(rate_per_km=2)
    ride1.calculate_fare(distance=10)
    print("Receipt for Ride 1:")
    ride1.print_receipt()

    # Second taxi ride
    ride2 = TaxiRide(rate_per_km=3)
    ride2.calculate_fare(distance=15)
    print("\nReceipt for Ride 2:")
    ride2.print_receipt()

if __name__ == "__main__":
    main()
