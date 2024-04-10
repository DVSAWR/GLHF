import re

mystr = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', mystr)
if match:
    print('found:', match.group())
else:
    print('not found')

print('\n---- Основные примеры ----')

match = re.search(r'iii', 'piiig')
print(match)
print(match.group())

match = re.search(r'igs', 'piiig')
print(match)

match = re.search(r'..g', 'piiig')
print(match)
print(match.group())

print('\n---- Повторение ----')

match = re.search(r'pi+', 'piiig')
print(match)
print(match.group())

match = re.search(r'i+', 'piiig')
print(match)
print(match.group())

match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
print(match)
print(match.group())
match = re.search(r'\d\s*\d\s*\d', 'xx12   3xx')
print(match)
print(match.group())
match = re.search(r'\d\s*\d\s*\d', 'xx123xx')
print(match)
print(match.group())

print('\n---- Пример электронной почты ----')

mystr = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', mystr)
if match:
    print(match)
    print(match.group())

print('\n---- Квадратные скобки ----')

match = re.search(r'[\w.-]+@[\w.-]+', mystr)
if match:
    print(match)
    print(match.group())

print('\n---- Груповое извлечение ----')

mystr = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', mystr)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))

print('\n---- Найти все ----')

mystr = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

emails = re.findall(r'[\w.-]+@[\w.-]+', mystr)

for email in emails:
    print(email)

print('\n---- findall с файлами ----')

with open('README.md', 'r') as file:
    match = re.findall(r'REG\w+.\w+', file.read())
    if match:
        print(match)
    else:
        print('NO')

print('\n---- findall и группы ----')

mystr = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w.-]+)@([\w.-]+)', mystr)
print(tuples)
for t in tuples:
    print(f'{t[0]} -> {t[1]}')

print('\n---- Замена ----')

mystr = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
print(mystr)
emails = re.sub(r'([\w.-]+)@([\w.-]+)', r'\1@EMAIL.COM', mystr)
print(emails)
