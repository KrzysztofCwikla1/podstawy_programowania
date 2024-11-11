###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input('...: ')

bank = swift[:4]

country_code = swift[4:6]

location = swift[6:8]

branch = swift[8:12] or None

print(f'Bank Code: {bank}')
print(f'Country Code: {country_code}')
print(f'Location Code: {location}')
print(f'Branch Code: {branch}')