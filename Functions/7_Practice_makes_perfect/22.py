def f(name):
    words = name.split()
    acronym = ""
    for word in words:
        acronym += word[0]
    return acronym

if __name__ == "__main__":
    print(f("Internet of Things"))       # Output: "IoT"
    print(f("For Your Information"))     # Output: "FYI"
    print(f("Python"))                   # Output: "P"