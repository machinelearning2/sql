#dictionaries

birthdays = {}

birthdays = {'Luke Skywalker': '5/24/19', 'Obi-Wan Kenobi': '3/11/57', 'Darth Vader': '4/1/41'}

if 'Yoda' in birthdays:
    print('yes, Yoda in Birthdays')
if 'Darth Vader' in birthdays:
    print('yes Darth Vader in Birthdays')

birthdays['Yoda'] = "unknown"
print(birthdays)
