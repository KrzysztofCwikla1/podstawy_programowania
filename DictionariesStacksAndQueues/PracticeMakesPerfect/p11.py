import json
import os

# File where voting data is stored
file_name = 'voting.json'

# Function to read the contents of the JSON file
def read_votes():
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    else:
        return {}

# Function to save the voting data to the JSON file
def save_votes(votes):
    with open(file_name, 'w') as file:
        json.dump(votes, file, indent=4)

# Read existing votes
votes = read_votes()

# Ask the user for their vote
person_name = input('Name of the person you are voting for: ')

# Update the vote count for the chosen person
if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

# Save updated voting data to the JSON file
save_votes(votes)

print(f"Vote for {person_name} has been recorded. Total votes: {votes[person_name]}")
