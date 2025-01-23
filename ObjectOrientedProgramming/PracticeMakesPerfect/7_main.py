class Statistics:
    def __init__(self):
        # Initialize an empty list to store numbers
        self.numbers = []

    def add_number(self, number):
        # Add a number to the list
        self.numbers.append(number)

    def display_numbers(self):
        # Display all numbers separated by a space
        print("Numbers:", " ".join(map(str, self.numbers)))

    def get_minimum(self):
        # Determine the smallest number
        return min(self.numbers) if self.numbers else None

    def get_maximum(self):
        # Determine the greatest number
        return max(self.numbers) if self.numbers else None

    def get_mean(self):
        # Calculate the arithmetic mean
        if not self.numbers:
            return None
        return sum(self.numbers) / len(self.numbers)

    def get_median(self):
        # Calculate the median
        if not self.numbers:
            return None
        sorted_numbers = sorted(self.numbers)
        n = len(sorted_numbers)
        mid = n // 2
        if n % 2 == 0:
            # If even, median is the average of the two middle values
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        else:
            # If odd, median is the middle value
            return sorted_numbers[mid]

    def print_statistics(self):
        # Print the calculated/determined statistical quantities
        print("Statistics:")
        print(f"Minimum: {self.get_minimum()}")
        print(f"Maximum: {self.get_maximum()}")
        print(f"Arithmetic Mean: {self.get_mean():.2f}")
        print(f"Median: {self.get_median():.2f}")


# Instantiate the class and perform the operations
statistics = Statistics()

# Add numbers to the set
numbers_to_add = [12, 37, 6, 9, 17]
for num in numbers_to_add:
    statistics.add_number(num)

# Display the numbers
statistics.display_numbers()

# Print the calculated statistics
statistics.print_statistics()

