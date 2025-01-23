import re 


email_file = 'report.txt'
...
...
with open(email_file, "r", encoding="utf-8") as file:
   email = file.read()

pattern = r"€\d+(?:\.\d{2})?"

amounts = re.findall(pattern, email)


amounts = [float(amount[1:]) for amount in amounts]

total = sum(amounts)

print(total)

