import re

mystr = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', mystr)
if match:
    print('found:', match.group())
else:
    print('not found')


print('')

match = re.search(r'iii', 'piiig')
print(match)
print(match.group())

match = re.search(r'igs', 'piiig')
print(match)

match = re.search(r'..g', 'piiig')
print(match)
print(match.group())




