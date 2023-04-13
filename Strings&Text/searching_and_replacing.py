"""
You want to search for and 
replace a text pattern in a string.

"""

# Example 1

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))


# Example 2

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))


# Example 3
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))