class Stadium:
    def __init__(self, sectors):
        self.sectors = sectors  # sectors is a dictionary, e.g., {"A": 120, "D": 150}

    def m1(self, sector, fans):
        # If sector exists, update its number of fans; otherwise, add it.
        self.sectors[sector] = fans

    def m2(self, sectors_str):
        # Sum of fans in the given sectors represented by the string.
        total_fans = 0
        for sector in sectors_str:
            if sector in self.sectors:
                total_fans += self.sectors[sector]
        return total_fans
def main():
    stadium = Stadium({"A": 120, "D": 150, "G": 90, "K": 110})

    # Modify fans in a sector
    stadium.m1("G", 130)

    # Calculate sum of fans in sectors "GD"
    print(stadium.m2("GD"))  # Output: 280

    # Calculate sum of fans in sectors "KEJ"
    print(stadium.m2("KEJ"))  # Output: 110

if __name__ == "__main__":
    main()