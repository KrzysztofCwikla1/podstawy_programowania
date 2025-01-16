import json

# Dictionary describing the book
favorite_book = {
    "title": "The Tower of the Swallow",
    "author": "Andrzej Sapkowski",
    "year": 1997,
    "genre": "Fantasy",
    "pages": 472
}

# Write the dictionary to a JSON file
with open("DictionariesStacksAndQueues\\PracticeMakesPerfect\\favourite.json", "w") as file:
    json.dump(favorite_book, file, indent=4)

print("Data has been written to favourite.json")