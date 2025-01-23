import re

with open("files.txt", "r", encoding="utf-8") as file:
    reader = file.read()

extension = r"[a-zA-Z0-9]+\.+[a-zA-Z]{4}"

pattern = re.findall(extension, reader)

print(pattern)