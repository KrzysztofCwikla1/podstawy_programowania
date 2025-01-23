import re

with open("email.txt", "r", encoding="utf-8") as file:
    email_content = file.read()


# Function to extract sender email address
def email_sender(email_content):
    pattern = r"From:\s*[^<]+<([^>]+)>"
    match = re.search(pattern, email_content)
    if match:
        return match.group(1)  # Return the email address
    return None

# Function to extract recipient email address
def email_recipient(email_content):
    pattern = r"To:\s*[^<]+<([^>]+)>"
    match = re.search(pattern, email_content)
    if match:
        return match.group(1)  # Return the email address
    return None

# Function to extract the email subject
def email_subject(email_content):
    pattern = r"Subject:\s*(.*)"
    match = re.search(pattern, email_content)
    if match:
        return match.group(1)  # Return the subject line
    return None

# Function to extract the email body
def email_body(email_content):
    pattern = r"\r?\n\r?\n(.*)"  # Match content after empty lines (body)
    match = re.search(pattern, email_content, re.DOTALL)  # DOTALL allows '.' to match newline characters
    if match:
        return match.group(1).strip()  # Return the body of the email
    return None



print(email_sender(email_content))

print(email_recipient(email_content))