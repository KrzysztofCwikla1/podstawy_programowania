# coordinates.py
class C:
    def __init__(self, points):
        self.points = points  # List of points, e.g., [[2,3],[1,8],[-6,4],[3,-7]]

    def m(self, n):
        # Returns True if at least n points are in the first quadrant, False otherwise.
        count = sum(1 for point in self.points if point[0] > 0 and point[1] > 0)
        return count >= n
def main():
    coords = C([[2, 3], [1, 8], [-6, 4], [3, -7]])

    print(coords.m(2))  # Output: True
    print(coords.m(3))  # Output: False

if __name__ == "__main__":
    main()