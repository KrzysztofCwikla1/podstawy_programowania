# Program to combine two contact lists and remove duplicates
contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

# Combining the lists using union operation to remove duplicates
merged_contacts = contacts_A | contacts_B
print("Merged contacts:", merged_contacts)
