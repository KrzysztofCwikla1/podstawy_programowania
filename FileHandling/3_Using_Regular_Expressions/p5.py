###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input("Enter username >>")
password = input("Enter password >>")

# pattern (criteria) for username and password
username_pattern = r"[a-z]{6,}"
password_pattern = r"[A-Za-z0-9_]{8,}"

# check if username and password are ok
username_match = re.fullmatch(username_pattern,username)
password_match = re.fullmatch(password_pattern, password)

# print results
if username_match and password_match:
   print("Ok")
else:
   print("Not ok") 