import re

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

text = "Alice was born on March 12, 1992. Her brother, John, was born on June 5, 1988. They have a mutual friend named Mike, whose phone number is 555-123-4567. In their hometown, which has a population of 1,234 or 1,235 people, a holiday festival is held every year on December 25. Alice works in an office with 30 employees. Her phone number is 555-765-4321."

month = "|".join(months)

date_pattern = rf"\b(?:{month}) \d{{1,2}}, \d{{4}}\b"
phone_pattern = r"\b[0-9]{3}\-[0-9]{3}\-[0-9]{4}\b"
decimal_pattern = r"\b[0-9]{1}\,[0-9]{3}\b"
name_pattern = r"[A-Z]{1}[a-z]{1,}"
number_pattern = r"[0-9]{2,}"

pattern = re.findall(date_pattern ,text)
pattern_2 = re.findall(phone_pattern, text)
pattern_3 = re.findall(decimal_pattern, text)
pattern_4 = re.findall(name_pattern, text)
pattern_5 = re.findall(number_pattern, text)

print(f"Dates: {pattern} \nPhone: {pattern_2} \nSeparated: {pattern_3} \nName: {pattern_4}, \nNumber: {pattern_5}")