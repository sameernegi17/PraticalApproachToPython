"""
You want to match or search text for a specific pattern.

"""

# Example 1

text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
text == 'yeah' # False
# Match at start or end
print(text.startswith('yeah')) # True
print(text.endswith('no')) # False
# Search for the location of the first occurrence
print(text.find('no')) # 10


# Example 2

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# Example 3

datepat = re.compile(r'\d+/\d+/\d+')

if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')
