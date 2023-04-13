# Example 4

import re

datepat = re.compile(r'\d+/\d+/\d+')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text)) # ['11/27/2012', '3/13/2013']

# Example 5
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')

print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

#Example 6
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.findall(text))

#iteratively
for m in datepat.finditer(text):
    print(m.groups())