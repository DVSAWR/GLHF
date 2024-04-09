import re


def preview(x):
    print(f'\n---- {x} ----')


preview('re')
#

preview('re.compile')
# Compile a regular expression pattern into a regular expression object, which can be used for matching using its match(), search() and other methods, described below.
my_string = 'QWE-qwe-123@mail.com'

prog = re.compile(r'\w\w')
result = prog.match(my_string)
print(result)
print(result.group())

result = re.match(r'\w\w', my_string)
print(result)
print(result.group())

preview('re.search')
# Scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding Match. Return None if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.
