# Completing the program to find spam emails in the received emails list
emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
spam_list = {"spam1@example.com", "spam2@example.com"}

# Finding the intersection of received emails and spam list to identify spam emails
spam_emails = emails_received & spam_list
print("Spam emails:", spam_emails)
